#!/bin/python3

import numpy as np
import os
from matplotlib import pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

def main():
  ch = 1.1e-7 # m2s-1
  t0 = float(input("Initial temperature [C] : ") or "10")
  t1 = float(input("Boundary temperature [C] : ") or "100")
  xmax = float(input("Thickness [cm] : ") or "1") * 0.005
  nsec = 100.0 * 2.5 * (xmax / 0.005)**2
  dt = 0.01 * (xmax / 0.005)**2
  dx = xmax / 25
  nx = int(xmax / dx)
  nstep = int(nsec / dt)

  # initialize
  tmp = np.full((nx,), t0)
  tmp[0] = t1
  dtmp = np.empty((nx,))
  os.system("mkdir -p img")
  os.system("rm -f img/*")

  for i in range(nstep):
    if (i % 200 == 0):
      plot_snap(tmp, i, nx, xmax, dt, t0, t1)

    # boundary condition tmp[0] = t1, tmp[nx] = tmp[nx-1]
    dtmp[0] = 0.0
    dtmp[1:nx-1] = ch * dt * (tmp[2:nx] - 2.0 * tmp[1:nx-1] + tmp[0:nx-2]) / (dx * dx)
    dtmp[nx-1] = ch * dt * (tmp[nx-1] - 2.0 * tmp[nx-1] + tmp[nx-2]) / (dx * dx)
    tmp[:] = tmp[:] + dtmp[:]

  os.system("convert -delay 10 -loop 0 ./img/*.png ./img/all.gif")
  os.system("rm -f img/*.png")

def plot_snap(tmp, i, nx, xmax, dt, t0, t1):
  cdict1 = {'red':   ((0.0, 1.0, 1.0),
                      (0.5, 1.0, 1.0),
                      (0.8, 0.6, 0.6),
                      (1.0, 0.6, 0.6)),
            'green': ((0.0, 0.2, 0.2),
                      (0.5, 0.2, 0.2),
                      (0.8, 0.5, 0.5),
                      (1.0, 0.5, 0.5)),
            'blue':  ((0.0, 0.3, 0.3),
                      (0.5, 0.3, 0.3),
                      (0.8, 0.4, 0.4),
                      (1.0, 0.4, 0.4)) }
  mycm = LinearSegmentedColormap('mycm', cdict1)

  data = np.zeros((nx*2,1))
  data[0:nx,   0] = tmp
  data[nx:2*nx,0] = tmp[::-1]
  fig, ax = plt.subplots(1)
  map1 = ax.pcolor(data, cmap=mycm)
  map1.set_clim(0, 100.0)
  plt.tick_params(axis="x", which="both", bottom="off", top="off", labelbottom="off")
  plt.tick_params(axis="y", which="both", left="off", right="off", labelleft="off")
  cbar = plt.colorbar(map1)
  plt.title("[%d cm, init %i deg, boundary %i deg] t = %isec" % (xmax*2*100, t0, t1, i*dt))
  plt.savefig("./img/%06i.png" % i)
  plt.close()

main()
