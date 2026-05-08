"""
Interactive Ellipsoid Visualization Tool - Streamlit Version
============================================================
Demonstrates that the projected (observed) axis ratio q_proj = b_proj / a_proj
is always >= c/a for any projection direction, as proven via the Poincaré
(Cauchy interlacing) theorem applied to the ellipsoid shape tensor.

See docs/MATH_PROOF.md for the full mathematical derivation.

Usage:
    streamlit run app.py
"""

import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from matplotlib.figure import Figure

# Configure font
def setup_font():
    """Configure matplotlib for better rendering"""
    # Set high DPI for better quality
    plt.rcParams['figure.dpi'] = 150
    plt.rcParams['savefig.dpi'] = 150
    
    # Solve minus sign display issue
    plt.rcParams['axes.unicode_minus'] = False

# Initialize font settings
setup_font()


def generate_ellipsoid(a, b, c, n=50):
    """
    Generate points on ellipsoid surface
    
    Parameters:
    -----------
    a, b, c : float
        Semi-axes lengths of the ellipsoid
    n : int
        Grid density
        
    Returns:
    --------
    X, Y, Z : ndarray
        Coordinates of ellipsoid surface
    """
    u = np.linspace(0, 2 * np.pi, n)
    v = np.linspace(0, np.pi, n)
    
    x = a * np.outer(np.cos(u), np.sin(v))
    y = b * np.outer(np.sin(u), np.sin(v))
    z = c * np.outer(np.ones(np.size(u)), np.cos(v))
    
    return x, y, z


def project_to_2d(a, b, c, azim, elev):
    """
    Project ellipsoid to 2D plane and calculate projection axis ratio
    
    Parameters:
    -----------
    a, b, c : float
        Semi-axes lengths of the ellipsoid
    azim : float
        Azimuth angle (degrees)
    elev : float
        Elevation angle (degrees)
        
    Returns:
    --------
    projected_points : ndarray
        2D projected points
    axis_ratio : float
        Projection axis ratio (minor/major)
    major_axis : float
        Major axis length
    minor_axis : float
        Minor axis length
    """
    # For standard views, use exact theoretical values
    if azim == 0 and elev == 90:  # XY plane (top view)
        major_axis = a
        minor_axis = b
        axis_ratio = b / a
        # Generate points for visualization
        u = np.linspace(0, 2 * np.pi, 100)
        proj_x = a * np.cos(u)
        proj_y = b * np.sin(u)
        proj_points = np.stack([proj_x, proj_y], axis=1)
        return proj_points, axis_ratio, major_axis, minor_axis
    elif azim == 0 and elev == 0:  # XZ plane (front view)
        major_axis = a
        minor_axis = c
        axis_ratio = c / a
        u = np.linspace(0, 2 * np.pi, 100)
        proj_x = a * np.cos(u)
        proj_y = c * np.sin(u)
        proj_points = np.stack([proj_x, proj_y], axis=1)
        return proj_points, axis_ratio, major_axis, minor_axis
    elif azim == 90 and elev == 0:  # YZ plane (side view)
        major_axis = b
        minor_axis = c
        axis_ratio = c / b
        u = np.linspace(0, 2 * np.pi, 100)
        proj_x = b * np.cos(u)
        proj_y = c * np.sin(u)
        proj_points = np.stack([proj_x, proj_y], axis=1)
        return proj_points, axis_ratio, major_axis, minor_axis
    
    # For custom views, use numerical calculation
    # Generate ellipsoid surface points (denser for projection calculation)
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 50)
    
    x = a * np.outer(np.cos(u), np.sin(v))
    y = b * np.outer(np.sin(u), np.sin(v))
    z = c * np.outer(np.ones(np.size(u)), np.cos(v))
    
    # Convert to radians
    azim_rad = np.radians(azim)
    elev_rad = np.radians(elev)
    
    # View direction vector
    cos_az = np.cos(azim_rad)
    sin_az = np.sin(azim_rad)
    cos_el = np.cos(elev_rad)
    sin_el = np.sin(elev_rad)
    
    view_x = cos_el * cos_az
    view_y = cos_el * sin_az
    view_z = sin_el
    
    # Construct orthonormal basis (screen x and y directions)
    up = np.array([0, 0, 1])
    
    # Right vector = up × view
    right = np.cross(up, [view_x, view_y, view_z])
    right = right / np.linalg.norm(right)
    
    # Recalculate up vector = view × right
    up_new = np.cross([view_x, view_y, view_z], right)
    up_new = up_new / np.linalg.norm(up_new)
    
    # Project all points to screen coordinate system
    points_3d = np.stack([x.flatten(), y.flatten(), z.flatten()], axis=1)
    
    proj_x = np.dot(points_3d, right)
    proj_y = np.dot(points_3d, up_new)
    
    # Calculate projection ellipse axes
    proj_points = np.stack([proj_x, proj_y], axis=1)
    
    # Center
    mean_point = np.mean(proj_points, axis=0)
    centered = proj_points - mean_point
    
    # Compute covariance matrix
    cov = np.cov(centered.T)
    
    # Eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(cov)
    
    # Sort eigenvalues (descending)
    idx = eigenvalues.argsort()[::-1]
    eigenvalues = eigenvalues[idx]
    
    # Major and minor axis lengths (using standard deviation)
    major_axis = 2 * np.sqrt(eigenvalues[0])
    minor_axis = 2 * np.sqrt(eigenvalues[1])
    
    # Axis ratio
    axis_ratio = minor_axis / major_axis if major_axis > 0 else 0
    
    return proj_points, axis_ratio, major_axis, minor_axis


def plot_3d_ellipsoid(ax, a, b, c, azim, elev, title):
    """Plot ellipsoid on specified 3D axes"""
    ax.clear()
    
    # Generate ellipsoid
    x, y, z = generate_ellipsoid(a, b, c)
    
    # Plot ellipsoid surface
    ax.plot_surface(x, y, z, alpha=0.7, cmap='viridis', edgecolor='none')
    
    # Plot coordinate axes
    max_val = max(a, b, c) * 1.2
    ax.plot([0, max_val], [0, 0], [0, 0], 'r-', linewidth=2, label='X')
    ax.plot([0, 0], [0, max_val], [0, 0], 'g-', linewidth=2, label='Y')
    ax.plot([0, 0], [0, 0], [0, max_val], 'b-', linewidth=2, label='Z')
    
    # Set viewing angle
    ax.view_init(elev=elev, azim=azim)
    
    # Set axis limits and labels
    ax.set_xlim([-max_val, max_val])
    ax.set_ylim([-max_val, max_val])
    ax.set_zlim([-max_val, max_val])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(title, fontsize=10)
    
    # Set equal aspect ratio
    ax.set_box_aspect([1, 1, 1])


def plot_2d_projection(ax, a, b, c, azim, elev, title):
    """Plot projection on specified 2D axes with axis ratio information"""
    ax.clear()
    
    # Get projection data
    proj_points, axis_ratio, major_axis, minor_axis = project_to_2d(a, b, c, azim, elev)
    
    # Plot projection points
    ax.scatter(proj_points[:, 0], proj_points[:, 1], s=1, alpha=0.5, c='blue')
    
    # Set axis properties
    max_val = max(a, b, c) * 1.2
    ax.set_xlim([-max_val, max_val])
    ax.set_ylim([-max_val, max_val])
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    
    # Title with axis ratio information
    info_text = f'{title}\nAxis Ratio q = {axis_ratio:.3f}\nMajor = {major_axis:.3f}\nMinor = {minor_axis:.3f}'
    ax.set_title(info_text, fontsize=9)


def create_visualization(a, b, c, azim, elev):
    """Create complete visualization figure"""
    # Create figure with high DPI
    fig = Figure(figsize=(16, 10), dpi=150)
    
    # Create subplot layout
    # Top row: Four 3D projection views
    ax_xy = fig.add_subplot(2, 4, 1, projection='3d')
    ax_xz = fig.add_subplot(2, 4, 2, projection='3d')
    ax_yz = fig.add_subplot(2, 4, 3, projection='3d')
    ax_custom = fig.add_subplot(2, 4, 4, projection='3d')
    
    # Bottom row: Four 2D projection views
    ax_proj_xy = fig.add_subplot(2, 4, 5)
    ax_proj_xz = fig.add_subplot(2, 4, 6)
    ax_proj_yz = fig.add_subplot(2, 4, 7)
    ax_proj_custom = fig.add_subplot(2, 4, 8)
    
    # Adjust subplot spacing - reduced vertical spacing
    fig.subplots_adjust(left=0.05, right=0.95, top=0.92, bottom=0.05, 
                       hspace=0.15, wspace=0.3)
    
    # Plot 3D views
    plot_3d_ellipsoid(ax_xy, a, b, c, azim=0, elev=90, title='XY Plane (Top View)')
    plot_3d_ellipsoid(ax_xz, a, b, c, azim=0, elev=0, title='XZ Plane (Front View)')
    plot_3d_ellipsoid(ax_yz, a, b, c, azim=90, elev=0, title='YZ Plane (Side View)')
    plot_3d_ellipsoid(ax_custom, a, b, c, azim=azim, elev=elev, 
                     title=f'Custom View\n(Azim={azim:.0f}°, Elev={elev:.0f}°)')
    
    # Plot 2D projection views
    plot_2d_projection(ax_proj_xy, a, b, c, azim=0, elev=90, title='XY Projection')
    plot_2d_projection(ax_proj_xz, a, b, c, azim=0, elev=0, title='XZ Projection')
    plot_2d_projection(ax_proj_yz, a, b, c, azim=90, elev=0, title='YZ Projection')
    plot_2d_projection(ax_proj_custom, a, b, c, azim=azim, elev=elev, title='Custom Projection')
    
    # Add 3D axis ratio information to figure title
    ratio_3d_ba = b / a if a > 0 else 0
    ratio_3d_ca = c / a if a > 0 else 0
    ratio_3d_cb = c / b if b > 0 else 0
    
    info_text = (f'Ellipsoid Parameters: a={a:.2f}, b={b:.2f}, c={c:.2f} | '
                f'3D Axis Ratios: b/a={ratio_3d_ba:.3f}, c/a={ratio_3d_ca:.3f}, c/b={ratio_3d_cb:.3f}')
    fig.suptitle(info_text, fontsize=14, fontweight='bold')
    
    return fig


def main():
    """Streamlit main function"""
    st.set_page_config(page_title="Interactive Ellipsoid Visualization", layout="wide")
    
    st.title("🌐 Interactive Ellipsoid Visualization Tool")
    st.markdown("### Study the Relationship Between 2D and 3D Axis Ratios")
    
    # Create sidebar control panel
    st.sidebar.header("📊 Parameter Controls")
    
    # Ellipsoid parameters
    st.sidebar.subheader("Ellipsoid Axes")
    a = st.sidebar.slider("a-axis (longest)", 0.5, 5.0, 3.0, 0.1)
    b = st.sidebar.slider("b-axis (intermediate)", 0.5, 5.0, 2.0, 0.1)
    c = st.sidebar.slider("c-axis (shortest)", 0.5, 5.0, 1.0, 0.1)
    
    st.sidebar.markdown("---")
    
    # Viewing angle parameters
    st.sidebar.subheader("Custom Viewing Angle")
    
    # Azimuth - slider and input box
    col1, col2 = st.sidebar.columns([3, 1])
    with col1:
        azim_slider = st.slider("Azimuth", 0, 360, 45, 1, key="azim_slider")
    with col2:
        azim_input = st.number_input("°", 0, 360, azim_slider, 1, key="azim_input", label_visibility="collapsed")
    
    # Use input value if different
    azim = azim_input if azim_input != azim_slider else azim_slider
    
    # Elevation - slider and input box
    col3, col4 = st.sidebar.columns([3, 1])
    with col3:
        elev_slider = st.slider("Elevation", -90, 90, 30, 1, key="elev_slider")
    with col4:
        elev_input = st.number_input("°", -90, 90, elev_slider, 1, key="elev_input", label_visibility="collapsed")
    
    # Use input value if different
    elev = elev_input if elev_input != elev_slider else elev_slider
    
    st.sidebar.markdown("---")
    
    # Preset cases
    st.sidebar.subheader("📋 Quick Presets")
    if st.sidebar.button("Oblate Spheroid (a=b>c)"):
        st.session_state.preset = {"a": 3.0, "b": 3.0, "c": 1.0}
    if st.sidebar.button("Prolate Ellipsoid (a>b>c)"):
        st.session_state.preset = {"a": 4.0, "b": 2.0, "c": 1.0}
    if st.sidebar.button("Sphere (a=b=c)"):
        st.session_state.preset = {"a": 3.0, "b": 3.0, "c": 3.0}
    
    # Apply preset
    if 'preset' in st.session_state and st.session_state.preset:
        a = st.session_state.preset["a"]
        b = st.session_state.preset["b"]
        c = st.session_state.preset["c"]
        st.session_state.preset = None
        st.rerun()
    
    # Display instructions
    with st.expander("ℹ️ Instructions", expanded=False):
        st.markdown("""
        ### Control Methods
        1. **Slider Control**: Drag sliders on the left to adjust parameters
        2. **Precise Input**: Enter exact values in input boxes next to sliders
        3. **Quick Presets**: Click preset buttons to load common configurations
        
        ### View Description
        - **Top Row**: 4 3D ellipsoid views (XY, XZ, YZ planes + Custom view)
        - **Bottom Row**: 4 corresponding 2D projection views showing projection axis ratios
        
        ### Research Goals
        - Observe how the same 3D ellipsoid's 2D axis ratio changes with different projection angles
        - Explore the relationship between 3D true axis ratios and 2D observed axis ratios
        - Understand the impact of viewing angle on shape measurements
        """)
    
    # Create and display visualization
    fig = create_visualization(a, b, c, azim, elev)
    st.pyplot(fig)
    
    # Display detailed information
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("3D Ratio b/a", f"{b/a:.3f}")
        st.metric("3D Ratio c/a", f"{c/a:.3f}")
    
    with col2:
        st.metric("3D Ratio c/b", f"{c/b:.3f}")
        st.metric("Current Azimuth", f"{azim}°")
    
    with col3:
        # Calculate custom view projection axis ratio
        _, ratio, _, _ = project_to_2d(a, b, c, azim, elev)
        st.metric("Custom Projection Ratio", f"{ratio:.3f}")
        st.metric("Current Elevation", f"{elev}°")


if __name__ == "__main__":
    main()
