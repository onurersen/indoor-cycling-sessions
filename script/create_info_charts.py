# !/usr/bin/env python
# title           : create_info_charts.py
# description     : Draws charts on data of sessions given as input
# author          : Berat Onur Ersen (onurersen@gmail.com)
# date            : 20190221
# version         : 1.0
# usage           : python create_info_charts.py
# notes           :
# python_version  :3.6.5
# ==============================================================================
import numpy as np
import matplotlib.pyplot as plt
import os
import shutil
from matplotlib import rcParams
import datetime
import errno

def main():
    try:
        try:
            os.makedirs("../charts")
        except OSError as e:
            if e.errno == errno.EEXIST:
                print("charts directory already exists, emptying...")
                shutil.rmtree("../charts", ignore_errors=True)
                os.makedirs("../charts")
            else:
                raise
        dates = ()
        calories = []
        kilometers = []
        max_kilometer_hour = []
        avg_kilometer_hour = []
        zone1_duration = []
        zone2_duration = []
        zone3_duration = []
        zone4_duration = []
        zone5_duration = []
        rpm_avg = []
        rpm_max = []
        duration_total = []
        duration_sum = 0.0
        with open('../report/session_info.txt', 'rU') as f:
            for line in f:
                if len(line.strip()) != 0:
                    if line.startswith("DATE") or "DATE" in line:
                        dates = dates + (line.split()[1],)
                    if line.startswith("CALORIES") or "CALORIES" in line:
                        calories.append(float((line.split(" ")[1]).strip()))
                    if line.startswith("KILOMETERS") or "KILOMETERS" in line:
                        kilometers.append(float((line.split(" ")[1]).strip()))
                    if line.startswith("KM/H") or "KM/H" in line:
                        max_kilometer_hour.append(float((line[4:].split("/")[0]).strip()))
                        avg_kilometer_hour.append(float((line[4:].split("/")[1]).strip()))
                    if line.startswith("ZONE1") or line.startswith("ZONE 1") or "ZONE1" in line or "ZONE 1" in line:
                        min_sec = [int(n) for n in ((line.split('/')[1]).strip()).split(':')]
                        value = float(min_sec[0]) + (min_sec[1] / float(60))
                        zone1_duration.append(float("%.2f" % value))
                        duration_in_secs = min_sec[0] * 60 + min_sec[1]
                        duration_sum = duration_sum + (duration_in_secs / float(60))
                        duration_total.append(float("%.2f" % duration_sum))
                        duration_sum = 0.0
                    if line.startswith("ZONE2") or line.startswith("ZONE 2") or "ZONE2" in line or "ZONE 2" in line:
                        min_sec = [int(n) for n in ((line.split('/')[1]).strip()).split(':')]
                        value = float(min_sec[0]) + (min_sec[1] / float(60))
                        zone2_duration.append(float("%.2f" % value))
                        duration_in_secs = (min_sec[0] * 60) + min_sec[1]
                        duration_sum = duration_sum + (duration_in_secs / float(60))
                    if line.startswith("ZONE3") or line.startswith("ZONE 3") or "ZONE3" in line or "ZONE 3" in line:
                        min_sec = [int(n) for n in ((line.split('/')[1]).strip()).split(':')]
                        value = float(min_sec[0]) + (min_sec[1] / float(60))
                        zone3_duration.append(float("%.2f" % value))
                        duration_in_secs = (min_sec[0] * 60) + min_sec[1]
                        duration_sum = duration_sum + (duration_in_secs / float(60))
                    if line.startswith("ZONE4") or line.startswith("ZONE 4") or "ZONE4" in line or "ZONE 4" in line:
                        min_sec = [int(n) for n in ((line.split('/')[1]).strip()).split(':')]
                        value = float(min_sec[0]) + (min_sec[1] / float(60))
                        zone4_duration.append(float("%.2f" % value))
                        duration_in_secs = (min_sec[0] * 60) + min_sec[1]
                        duration_sum = duration_sum + (duration_in_secs / float(60))
                    if line.startswith("ZONE5") or line.startswith("ZONE 5") or "ZONE5" in line or "ZONE 5" in line:
                        min_sec = [int(n) for n in ((line.split('/')[1]).strip()).split(':')]
                        value = float(min_sec[0]) + (min_sec[1] / float(60))
                        zone5_duration.append(float("%.2f" % value))
                        duration_in_secs = (min_sec[0] * 60) + min_sec[1]
                        duration_sum = duration_sum + (duration_in_secs / float(60))
                    if line.startswith("RPM") or "RPM" in line:
                        rpm_avg.append(float((line[3:].split("/")[0]).strip()))
                        rpm_max.append(float((line[3:].split("/")[1]).strip()))

        draw_graph(dates, calories, "Calories Burnt", "Calories", "calories_burnt")
        draw_graph(dates, kilometers, "Kilometer Range", "Kilometers ", "kilometers")
        draw_graph(dates, max_kilometer_hour, "Maximum KM/H", "KM/H", "max_km_h")
        draw_graph(dates, avg_kilometer_hour, "Average KM/H", "KM/H", "avg_km_h")
        draw_graph(dates, zone1_duration, "ZONE-1 Duration", "Duration (in minutes)", "zone1_duration")
        draw_graph(dates, zone2_duration, "ZONE-2 Duration", "Duration (in minutes)", "zone2_duration")
        draw_graph(dates, zone3_duration, "ZONE-3 Duration", "Duration (in minutes)", "zone3_duration")
        draw_graph(dates, zone4_duration, "ZONE-4 Duration", "Duration (in minutes)", "zone4_duration")
        draw_graph(dates, zone5_duration, "ZONE-5 Duration", "Duration (in minutes)", "zone5_duration")
        draw_graph(dates, duration_total, "Total Duration", "Total Duration (in minutes)", "total_duration")
        draw_graph(dates, rpm_avg, "Average RPM", "RPM", "avg_rpm")
        draw_graph(dates, rpm_max, "Maximum RPM", "RPM", "max_rpm")
    except Exception as e:
        print(e)


def draw_graph(axis_x_data, axis_y_data, chart_title, y_axis_label, filename):
    try:
        x_positions = np.arange(len(axis_x_data))
        plt.gcf().subplots_adjust(bottom=0.25)
        plt.plot(x_positions, axis_y_data)
        plt.xticks(x_positions, axis_x_data)
        plt.xticks(fontsize=8, rotation=60)
        plot_font = {'family': 'sans-serif', 'weight': 'normal', 'size': 8.0}
        plt.rc('font', **plot_font)
        plt.gcf().set_size_inches((5, 4))
        plt.ylabel(y_axis_label, fontsize=10)
        plt.title(chart_title, fontsize=10)
        labels = axis_y_data
        for label, x, y in zip(labels, x_positions, axis_y_data):
            plt.annotate(label, xy=(x, y), xytext=(x, y))
        plt.savefig("../charts/" + filename + '.png')
        plt.clf()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()




