import streamlit as st

st.set_page_config(layout="wide")

#st.title("Cheat Sheet :tea: :coffee:")

col1, col2, col3 = st.columns(3, gap="medium")

with col1:

    st.image("static/matplotlib.jpg", use_column_width=True)
    st.markdown("<span style='background-color:lightgrey; padding:10px; font-weight:bold; display:flex;'>Quick Start</span> ", unsafe_allow_html=True)
    st.code('''
    import numpy as np
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    X = np.linspace(0, 2*np.pi, 100)
    Y = np.cos(X)
    fig, ax = plt.subplots()
    ax.plot(X, Y, color=’green’)
    fig.savefig(“figure.pdf”)
    fig.show()
    ''')

    st.info("Anatomy of a figure")    
    st.image("static/anatomy_of_figure.jpg", use_column_width=True)

    st.success("Subplots layout")

    col11, col12 = st.columns([1,4])
    with col11:
        st.image("static/layout1.jpg", use_column_width=True)
    with col12:
        st.markdown("**subplot[s]**(rows,cols,…)")
        st.caption("fig, axs = plt.subplots(3, 3)")

    col11, col12 = st.columns([1,4])
    with col11:
        st.image("static/layout2.jpg", use_column_width=True)
    with col12:
        st.markdown("G = **gridspec**(rows,cols,…)")
        st.caption("ax = G[0,:]")

    col11, col12 = st.columns([1,4])
    with col11:
        st.image("static/layout3.jpg", use_column_width=True)
    with col12:
        st.markdown("ax.**inset_axes**(extent)")

    col11, col12 = st.columns([1,4])
    with col11:
        st.image("static/layout4.jpg", use_column_width=True)
    with col12:
        st.markdown("d=**make_axes_locatable**(ax)")
        st.caption("ax = d.new_horizontal(’10%’)")

    st.info("Getting help")

    col11, col12 = st.columns([1,10])
    with col11:
        st.image("static/matplotlib.png", use_column_width=True)
    with col12:
        st.markdown("<a href='https://matplotlib.org/'>matplotlib.org</a>", unsafe_allow_html=True)

    col11, col12 = st.columns([1,10])
    with col11:
        st.image("static/github.png", use_column_width=True)
    with col12:
        st.markdown("<a href='https://github.com/matplotlib/matplotlib/issues'>github.com/matplotlib/matplotlib/issues</a>", unsafe_allow_html=True)

    col11, col12 = st.columns([1,10])
    with col11:
        st.image("static/discourse.png", use_column_width=True)
    with col12:
        st.markdown("<a href='https://discourse.matplotlib.org/'>discourse.matplotlib.org</a>", unsafe_allow_html=True)

    col11, col12 = st.columns([1,10])
    with col11:
        st.image("static/stackoverflow.png", use_column_width=True)
    with col12:
        st.markdown("<a href='https://stackoverflow.com/questions/tagged/matplotlib'>stackoverflow.com/questions/tagged/matplotlib</a>", unsafe_allow_html=True)

    col11, col12 = st.columns([1,10])
    with col11:
        st.image("static/gitter.jpeg", use_column_width=True)
    with col12:
        st.markdown("<a href='https://app.gitter.im/#/room/#matplotlib_matplotlib'>https://app.gitter.im/#/room/#matplotlib_matplotlib</a>", unsafe_allow_html=True)

    col11, col12 = st.columns([1,10])
    with col11:
        st.image("static/twitter.png", use_column_width=True)
    with col12:
        st.markdown("<a href='https://twitter.com/matplotlib'>twitter.com/matplotlib</a>", unsafe_allow_html=True)

    col11, col12 = st.columns([1,10])
    with col11:
        st.image("static/mail.png", use_column_width=True)
    with col12:
        st.markdown("Matplotlib users mailing list", unsafe_allow_html=True)

with col2:
    st.markdown("<span style='background-color:lightgrey; padding:10px; font-weight:bold; display:flex;'>Basic plots</span> ", unsafe_allow_html=True)

    col21, col22 = st.columns([1,4])
    with col21:
        st.image("static/chart1.jpg", use_column_width=True)
    with col22:
        st.markdown("**plot**([X],Y,[fmt],…)")
        st.caption("X, Y, fmt, color, marker, linestyle")

    col21, col22 = st.columns([1,4])
    with col21:
        st.image("static/chart2.jpg", use_column_width=True)
    with col22:
        st.markdown("**scatter**(X,Y,…)")
        st.caption("X, Y, [s]izes, [c]olors, marker, cmap")

    col21, col22 = st.columns([1,4])
    with col21:
        st.image("static/chart3.jpg", use_column_width=True)
    with col22:
        st.markdown("**bar[h]**(x,height,…)")
        st.caption("x, height, width, bottom, align, color")

    col21, col22 = st.columns([1,4])
    with col21:
        st.image("static/chart4.jpg", use_column_width=True)
    with col22:
        st.markdown("**imshow**(Z,…)")
        st.caption("Z, cmap, interpolation, extent, origin")

    col21, col22 = st.columns([1,4])
    with col21:
        st.image("static/chart5.jpg", use_column_width=True)
    with col22:
        st.markdown("**contour[f]**([X],[Y],Z,…)")
        st.caption("X, Y, Z, levels, colors, extent, origin")

    st.info("Advanced plots")

    col21, col22 = st.columns([1,4])
    with col21:
        st.image("static/chart6.jpg", use_column_width=True)
    with col22:
        st.markdown("**step**(X,Y,[fmt],…)")
        st.caption("X, Y, fmt, color, marker, where")

    col21, col22 = st.columns([1,4])
    with col21:
        st.image("static/chart7.jpg", use_column_width=True)
    with col22:
        st.markdown("**boxplot**(X,…)")
        st.caption("X, notch, sym, bootstrap, widths")

    col21, col22 = st.columns([1,4])
    with col21:
        st.image("static/chart8.jpg", use_column_width=True)
    with col22:
        st.markdown("**errorbar**(X,Y,xerr,yerr,…)")
        st.caption("X, Y, xerr, yerr, fmt")

    col21, col22 = st.columns([1,4])
    with col21:
        st.image("static/chart9.jpg", use_column_width=True)
    with col22:
        st.markdown("**hist**(X, bins, …)")
        st.caption("X, bins, range, density, weights")

    col21, col22 = st.columns([1,4])
    with col21:
        st.image("static/chart10.jpg", use_column_width=True)
    with col22:
        st.markdown("**violinplot**(D,…)")
        st.caption("D, positions, widths, ver")    

    with col3:
        st.markdown("<span style='background-color:lightgrey; padding:10px; font-weight:bold; display:flex;'>Animation</span> ", unsafe_allow_html=True)
        st.code('''
            import matplotlib.animation as mpla
            T = np.linspace(0, 2*np.pi, 100)
            S = np.sin(T)
            line, = plt.plot(T, S)
            def animate(i):
                line.set_ydata(np.sin(T+i/50))
            anim = mpla.FuncAnimation(plt.gcf(), animate,
                                         interval=5)
            plt.show()
        ''')

        st.info("Styles")
        st.code("plt.style.use(style)")
        st.image("static/styles.jpg", use_column_width=True)

        st.success("Quick reminder")
        st.code('''
                ax.grid()
                ax.set_[xy]lim(vmin, vmax)
                ax.set_[xy]label(label)
                ax.set_[xy]ticks(ticks, [labels])
                ax.set_[xy]ticklabels(labels)
                ax.set_title(title)
                ax.tick_params(width=10, …)
                ax.set_axis_[on|off]()
                fig.suptitle(title)
                fig.tight_layout()
                plt.gcf(), plt.gca()
                mpl.rc(’axes’, linewidth=1, …)
                [fig|ax].patch.set_alpha(0)
                text=r’$\frac{-e^{i\pi}}{2^n}$’
        ''')

        st.info("Ten simple rules")
        st.markdown('''
            1. Know your audience
            2. Identify your message
            3. Adapt the figure
            4. Captions are not optional
            5. Do not trust the defaults
            6. Use color effectively
            7. Do not mislead the reader
            8. Avoid “chartjunk”
            9. Message trumps beauty
            10. Get the right tool
        ''')