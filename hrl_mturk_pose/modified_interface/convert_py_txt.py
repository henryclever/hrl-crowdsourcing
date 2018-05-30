#!/usr/bin/env python

#By Henry M. Clever
#This code to make pickle files is a combination of head_detector_bagreading.py (written by Ari Kapusta) and bag_to_p.py (written by Yash Chitalia).
#The original bag_to_p.py requires replaying the bag files at original speed, which is cumbersome.
#This version speeds up the latter and makes a pickle file that is better annotated

import Image
import rospy, roslib
import sys, os
import random, math
import numpy as np
import matplotlib.pyplot as plt
import cPickle as pickle
from time import sleep
from scipy import ndimage
from geometry_msgs.msg import TransformStamped
from geometry_msgs.msg import PoseStamped
import rosbag
import copy
def load_pickle(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)


class converter():


    def visualize_pressure_map(self, p_map, block = True, title = ' '):
        #p_map_val[0, :, :] = p_map[1, : ,:]

        try:
            p_map = p_map[0,:,:] #select the original image matrix from the intermediate amplifier matrix and the height matrix
        except:
            pass

        plt.close()
        plt.pause(0.0001)

        fig = plt.gcf()
        mngr = plt.get_current_fig_manager()
        # to put it into the upper left corner for example:
        #mngr.window.setGeometry(50, 100, 840, 705)

        plt.pause(0.0001)



        ax1 = fig.add_subplot(1, 4, 1)
        xlim = [-2.0, 49.0]
        ylim = [86.0, -2.0]
        ax1.set_xlim(xlim)
        ax1.set_ylim(ylim)
        ax1.set_axis_bgcolor('cyan')
        ax1.imshow(p_map, interpolation='nearest', cmap=
        plt.cm.bwr, origin='upper', vmin=0, vmax=100)
        ax1.set_title('Pressure Mat')

        ax1 = fig.add_subplot(1, 4, 2)
        xlim = [-2.0, 49.0]
        ylim = [86.0, -2.0]
        ax1.set_xlim(xlim)
        ax1.set_ylim(ylim)
        ax1.set_axis_bgcolor('cyan')
        ax1.imshow(p_map, interpolation='nearest', cmap=
        plt.cm.bwr, origin='upper', vmin=0, vmax=100)
        ax1.set_title('Thermal Camera')


        ax1 = fig.add_subplot(1, 4, 3)
        xlim = [-2.0, 49.0]
        ylim = [86.0, -2.0]
        ax1.set_xlim(xlim)
        ax1.set_ylim(ylim)
        ax1.set_axis_bgcolor('cyan')
        ax1.imshow(p_map, interpolation='nearest', cmap=
        plt.cm.bwr, origin='upper', vmin=0, vmax=100)
        ax1.set_title('Depth Camera')


        ax1 = fig.add_subplot(1, 4, 4)
        xlim = [-2.0, 49.0]
        ylim = [86.0, -2.0]
        ax1.set_xlim(xlim)
        ax1.set_ylim(ylim)
        ax1.set_axis_bgcolor('cyan')
        ax1.imshow(p_map, interpolation='nearest', cmap=
        plt.cm.bwr, origin='upper', vmin=0, vmax=100)
        ax1.set_title('RGB Camera')

        fig.set_size_inches(16, 8)

        plt.show(block=False)

        plt.savefig('testplot.png', bbox_inches='tight')

        return


if __name__ == "__main__":
    data = load_pickle('/home/henry/test/trainval4_150rh1_sit120rh.p')


    for item in data:
        print item

    data['images'] = np.array(data['images'])

    print data['images'].shape
    print len(data['images'])
    print len(data['images'][0])
    #print data['images'][0]


    p_map = np.reshape(data['images'][0], (84, 47))
    print p_map.shape

    converter().visualize_pressure_map(p_map)

    #np.savetxt('/home/henry/test/one_sample.txt',data['images'][0])

    #print 'Finished with txt'

    #pickle.dump(data['images'],open(os.path.join('/home/henry/test/trainval4_150rh1_sit120rh_imgonly.p'), 'wb'))

    print 'Finished!'