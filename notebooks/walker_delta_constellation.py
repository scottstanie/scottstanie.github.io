import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.patches import Circle
    import cartopy.crs as ccrs
    return ccrs, mo, np, plt


@app.cell
def _(mo):
    mo.md("""
    # Walker Delta Constellation Visualizer

    Explore how the Walker Delta parameters affect satellite constellation geometry and ground tracks.

    **Notation: i: t/p/f**
    - **i** = inclination (degrees)
    - **t** = total number of satellites
    - **p** = number of orbital planes
    - **f** = phasing factor (0 to p-1)
    """)
    return


@app.cell
def _(mo):
    # Walker Delta parameters
    inclination_slider = mo.ui.slider(
        start=0, stop=90, step=1, value=56, label="Inclination i (°)"
    )

    total_sats_slider = mo.ui.slider(
        start=3, stop=36, step=1, value=24, label="Total satellites t"
    )

    num_planes_slider = mo.ui.slider(
        start=1, stop=8, step=1, value=3, label="Number of planes p"
    )

    phasing_slider = mo.ui.slider(
        start=0, stop=7, step=1, value=1, label="Phasing factor f"
    )

    # Orbital parameters
    altitude_slider = mo.ui.slider(
        start=400, stop=36000, step=100, value=23222, label="Altitude (km)"
    )

    # Time for ground track
    time_slider = mo.ui.slider(
        start=0.5,
        stop=24,
        step=0.5,
        value=6,
        label="Ground track duration (hours)",
    )

    mo.vstack(
        [
            mo.md("### Walker Parameters"),
            mo.hstack([inclination_slider, total_sats_slider]),
            mo.hstack([num_planes_slider, phasing_slider]),
            mo.md("### Orbital & Display Parameters"),
            mo.hstack([altitude_slider, time_slider]),
        ]
    )
    return (
        altitude_slider,
        inclination_slider,
        num_planes_slider,
        phasing_slider,
        time_slider,
        total_sats_slider,
    )


@app.cell
def _(
    altitude_slider,
    inclination_slider,
    mo,
    num_planes_slider,
    phasing_slider,
    time_slider,
    total_sats_slider,
):
    # Extract values
    inc = inclination_slider.value
    t = total_sats_slider.value
    p = num_planes_slider.value
    f = min(phasing_slider.value, p - 1)  # f should be 0 to p-1
    altitude = altitude_slider.value
    track_hours = time_slider.value

    sats_per_plane = t // p
    extra_sats = t % p

    # Phase offset between adjacent planes
    phase_offset = f * 360 / t if t > 0 else 0

    mo.md(f"""
    ### Current Configuration: {inc}°: {t}/{p}/{f}, **Altitude:** {altitude} km
    """)
    return (
        altitude,
        extra_sats,
        f,
        inc,
        p,
        phase_offset,
        sats_per_plane,
        t,
        track_hours,
    )


@app.cell
def _(np):
    # Constants
    R_EARTH = 6371  # km
    MU_EARTH = 398600.4418  # km³/s²
    OMEGA_EARTH = 7.2921159e-5  # rad/s (Earth rotation rate)


    def orbital_period(altitude_km):
        """Compute orbital period in seconds."""
        a = R_EARTH + altitude_km
        return 2 * np.pi * np.sqrt(a**3 / MU_EARTH)


    def compute_ground_track(
        inc_deg, raan_deg, ta0_deg, altitude_km, duration_hours, num_points=500
    ):
        """
        Compute ground track for a satellite.

        Returns arrays of (longitude, latitude) in degrees.
        """
        inc = np.radians(inc_deg)
        raan = np.radians(raan_deg)
        ta0 = np.radians(ta0_deg)

        a = R_EARTH + altitude_km
        T = orbital_period(altitude_km)
        n = 2 * np.pi / T  # mean motion

        duration_sec = duration_hours * 3600
        times = np.linspace(0, duration_sec, num_points)

        # True anomaly over time (circular orbit, so TA = MA)
        ta = ta0 + n * times

        # Position in orbital plane (perifocal frame, circular orbit)
        r = a  # constant for circular orbit

        # Convert to ECI coordinates
        # For circular orbit with omega=0 (argument of perigee = 0)
        x_eci = r * (
            np.cos(raan) * np.cos(ta) - np.sin(raan) * np.sin(ta) * np.cos(inc)
        )
        y_eci = r * (
            np.sin(raan) * np.cos(ta) + np.cos(raan) * np.sin(ta) * np.cos(inc)
        )
        z_eci = r * np.sin(ta) * np.sin(inc)

        # Earth rotation: convert ECI to ECEF
        theta = OMEGA_EARTH * times  # Earth rotation angle
        x_ecef = x_eci * np.cos(theta) + y_eci * np.sin(theta)
        y_ecef = -x_eci * np.sin(theta) + y_eci * np.cos(theta)
        z_ecef = z_eci

        # Convert ECEF to lat/lon
        lat = np.degrees(np.arcsin(z_ecef / r))
        lon = np.degrees(np.arctan2(y_ecef, x_ecef))

        return lon, lat


    def get_current_position(inc_deg, raan_deg, ta_deg, altitude_km):
        """Get current lat/lon for a satellite."""
        lon, lat = compute_ground_track(
            inc_deg, raan_deg, ta_deg, altitude_km, 0, num_points=1
        )
        return lon[0], lat[0]


    def build_constellation(inc, t, p, f):
        """
        Build Walker Delta constellation.

        Returns list of (plane_idx, raan, true_anomaly) for each satellite.
        """
        satellites = []
        sats_per_plane = t // p

        for plane_idx in range(p):
            raan = plane_idx * 360 / p
            phase_shift = plane_idx * f * 360 / t

            for sat_idx in range(sats_per_plane):
                ta = (sat_idx * 360 / sats_per_plane + phase_shift) % 360
                satellites.append((plane_idx, raan, ta))

        # Handle any remaining satellites (distribute to first planes)
        extra = t % p
        for i in range(extra):
            plane_idx = i
            raan = plane_idx * 360 / p
            phase_shift = plane_idx * f * 360 / t
            ta = (
                sats_per_plane * 360 / sats_per_plane + phase_shift + i * 360 / t
            ) % 360
            satellites.append((plane_idx, raan, ta))

        return satellites
    return (
        build_constellation,
        compute_ground_track,
        get_current_position,
        orbital_period,
    )


@app.cell
def _():
    return


@app.cell
def _(
    altitude,
    build_constellation,
    ccrs,
    compute_ground_track,
    f,
    get_current_position,
    inc,
    mo,
    np,
    orbital_period,
    p,
    plt,
    t,
    track_hours,
):
    # Build the constellation
    constellation = build_constellation(inc, t, p, f)

    # Compute ground tracks and positions
    ground_tracks = []
    current_positions = []

    for plane_idx, raan, ta in constellation:
        # Ground track
        lon, lat = compute_ground_track(inc, raan, ta, altitude, track_hours)
        ground_tracks.append((plane_idx, lon, lat))

        # Current position
        curr_lon, curr_lat = get_current_position(inc, raan, ta, altitude)
        current_positions.append((plane_idx, curr_lon, curr_lat))


    # Color map for different planes
    colors = plt.cm.tab10(np.linspace(0, 1, max(p, 1)))

    # fig, ax = plt.subplots(figsize=(14, 8), facecolor="#1a1a2e")
    # ax.set_facecolor("#16213e")

    fig = plt.figure(figsize=(12, 7))
    ax = fig.add_subplot(111, projection=ccrs.PlateCarree())
    ax.set_global()
    ax.stock_img()
    ax.coastlines()

    # # Draw a simple world map outline (coastlines approximation)
    # # Just draw the map boundaries for now
    # ax.set_xlim(-180, 180)
    # ax.set_ylim(-90, 90)

    # Grid
    ax.grid(True, alpha=0.3, color="white", linestyle="-", linewidth=0.5)
    ax.set_xticks(np.arange(-180, 181, 30))
    ax.set_yticks(np.arange(-90, 91, 30))

    # Draw equator and prime meridian
    ax.axhline(y=0, color="white", alpha=0.5, linewidth=1)
    ax.axvline(x=0, color="white", alpha=0.5, linewidth=1)

    # Draw inclination bands
    ax.axhline(y=inc, color="yellow", alpha=0.3, linewidth=1, linestyle="--")
    ax.axhline(y=-inc, color="yellow", alpha=0.3, linewidth=1, linestyle="--")
    ax.fill_between([-180, 180], -inc, inc, alpha=0.1, color="yellow")

    # Plot ground tracks
    for plane_idx, lon, lat in ground_tracks:
        # Handle longitude wrapping for cleaner plotting
        lon_wrapped = lon.copy()
        # Find discontinuities (jumps > 180°)
        diff = np.abs(np.diff(lon_wrapped))
        jump_indices = np.where(diff > 180)[0]

        # Insert NaN at discontinuities to break the line
        lon_plot = lon_wrapped.copy()
        lat_plot = lat.copy()

        for idx in reversed(jump_indices):
            lon_plot = np.insert(lon_plot, idx + 1, np.nan)
            lat_plot = np.insert(lat_plot, idx + 1, np.nan)

        ax.plot(
            lon_plot, lat_plot, color=colors[plane_idx], alpha=0.6, linewidth=1.5
        )

    # Plot current satellite positions
    for plane_idx, lon, lat in current_positions:
        ax.scatter(
            lon,
            lat,
            c=[colors[plane_idx]],
            s=100,
            edgecolors="white",
            linewidths=1.5,
            zorder=5,
        )

    # Labels and title
    ax.set_xlabel("Longitude (°)", color="white", fontsize=12)
    ax.set_ylabel("Latitude (°)", color="white", fontsize=12)
    ax.set_title(
        f"Walker Delta {inc}°: {t}/{p}/{f}  |  Altitude: {altitude} km  |  "
        f"Period: {orbital_period(altitude)/60:.1f} min",
        color="white",
        fontsize=14,
        fontweight="bold",
    )

    # Style tick labels
    ax.tick_params(colors="white")
    for spine in ax.spines.values():
        spine.set_color("white")
        spine.set_alpha(0.3)

    # Legend for planes
    legend_elements = [
        plt.Line2D(
            [0],
            [0],
            color=colors[i],
            linewidth=2,
            label=f"Plane {i+1} (RAAN={i*360/p:.0f}°)",
        )
        for i in range(p)
    ]
    ax.legend(
        handles=legend_elements,
        loc="upper right",
        facecolor="#1a1a2e",
        edgecolor="white",
        labelcolor="white",
    )

    # Summary table
    plane_summary = []
    for plane_idx in range(p):
        sats_in_plane = [
            (raan, ta) for pi, raan, ta in constellation if pi == plane_idx
        ]
        if sats_in_plane:
            raan = sats_in_plane[0][0]
            tas = [ta for _, ta in sats_in_plane]
            plane_summary.append(
                {
                    "Plane": plane_idx + 1,
                    "RAAN (°)": f"{raan:.1f}",
                    "Satellites": len(sats_in_plane),
                    "True Anomalies (°)": ", ".join(
                        [f"{ta:.1f}" for ta in sorted(tas)]
                    ),
                }
            )
    mo.md("### Constellation Details")
    mo.ui.table(plane_summary)


    plt.tight_layout()
    fig
    return


@app.cell
def _(extra_sats, mo, p, phase_offset, sats_per_plane):
    mo.md(f"""
    Current configuration:
    - **Satellites per plane:** {sats_per_plane} (+ {extra_sats} extra distributed)
    - **RAAN spacing:** {360/p:.1f}° between planes
    - **In-plane spacing:** {360/sats_per_plane:.1f}° between satellites
    - **Phase offset:** {phase_offset:.1f}° true anomaly shift per plane
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ---
    ### Notes

    - **Yellow dashed lines** show the inclination limits (±i°) — satellites never
      pass beyond these latitudes
    - **Ground tracks** show the path each satellite traces over Earth as it rotates
    - **Dots** show current satellite positions (at t=0)
    - The **phasing factor f** shifts satellites in adjacent planes, spreading coverage
      more evenly

    Try some famous constellations:
    - **Galileo:** 56°: 24/3/1
    - **GPS:** 55°: 24/6/1
    - **Iridium:** 86.4°: 66/6/2
    - **Starlink (shell 1):** 53°: 22/1/0 (single plane slice)
    """)
    return


if __name__ == "__main__":
    app.run()
