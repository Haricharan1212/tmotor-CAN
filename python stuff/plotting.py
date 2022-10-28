from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

fig = plt.figure()
ax1 = fig.add_subplot(1,3,1)
ax2 = fig.add_subplot(1,3,2)
ax3 = fig.add_subplot(1,3,3)


def animate(i):
    graph_data = open('output_data.txt','r').read()
    lines = graph_data.split('\n')
    t = []
    p = []
    v = []
    to = []
    th = []
    omg = []
    torq = []

    for line in lines:
        if len(line) > 1:
            time, theta, p_out,omega, v_out, torque, t_out = line.split(',')
            t.append(float(time))
            p.append(float(p_out))
            v.append(float(v_out))
            to.append(float(t_out))
            th.append(float(theta))
            omg.append(float(omega))
            torq.append(torque)

    ax1.clear()
    ax2.clear()
    ax3.clear()

    current_time = t[len(t) - 1]

    ax1.set_title("Position")
    ax2.set_title("Velocity")
    ax3.set_title("Torque")

    ax1.set_xlim(current_time - 20, current_time)
    ax2.set_xlim(current_time - 20, current_time)
    ax3.set_xlim(current_time - 20, current_time)

    ax1.set_ylim(-6.28, 6.28)
    ax2.set_ylim(-3, 3)
    ax3.set_ylim(-50, 50)


    ax1.plot(t, p)
    ax1.plot(t, th)
    ax2.plot(t, v)    
    ax2.plot(t, omg)
    ax3.plot(t, to)
    ax3.plot(t, torq)
    
    
ani = FuncAnimation(fig, animate, interval=1000)

plt.show()