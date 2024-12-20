<template>
  <div class="card">
    <div class="card-body">
      <h5 class="card-title">Installations over time</h5>
      <LineChart :chart-data="this.getChartData()" :options="chartOptions"/>
    </div>
  </div>
</template>

<script>
import {LineChart} from 'vue-chart-3';
import {Chart, registerables} from "chart.js";
import {interpolateTurbo} from "d3-scale-chromatic";
import {compareVersions} from "compare-versions";

Chart.register(...registerables);

export default {
  name: "HistoryChart",
  props: ["versions"],
  components: {
    LineChart
  },
  data() {
    return {
      chartOptions: {
        animation: false,
        tension: 0.1,
        showLine: true,
        plugins: {
          legend: {
            position: 'right'
          }
        }
      }
    }
  },
  computed: {
    sortedVersions() {
      return Object.keys(this.versions).map((key) => {
        return [key, this.versions[key]]
      }).sort((first, second) => {
        const cleanedFirst = this.cleanVersion(first[0])
        const cleanedSecond = this.cleanVersion(second[0])
        return compareVersions(cleanedFirst, cleanedSecond)
      })
    },
    chartColors() {
      // Create a dict of colors for versions
      const colors = this.generateColors(this.sortedVersions.length);
      const versions = this.sortedVersions.map(version => version[0])
      const dict = {}
      versions.forEach((version, index) => {
        dict[version] = colors[index]
      })
      return dict
    }
  },
  methods: {
    getChartData() {
      if (this.versions === undefined || this.versions.length === 0) {
        return {
          labels: [],
          datasets: []
        }
      }

      // Collect all dates for display
      const dates = new Set()
      for (const versionData of this.sortedVersions) {
        for (const date of Object.keys(versionData[1])) {
          dates.add(date)
        }
      }

      // Collect data for each date
      const dataSets = []
      for (const versionData of this.sortedVersions) {

        const data = []
        for (const date of Array.from(dates)) {
          data.push(versionData[1][date])
        }

        dataSets.push({
          label: versionData[0],
          backgroundColor: this.chartColors[versionData[0]],
          borderColor: this.chartColors[versionData[0]],
          data: data,
        })
      }

      return {
        labels: Array.from(dates),
        datasets: dataSets
      }
    }
    ,
    generateColors(dataLength,) {
      const colorStart = 0.04
      const colorEnd = 1
      const colorRange = colorEnd - colorStart;
      const intervalSize = colorRange / dataLength;
      let colorPoint;
      const colorArray = [];

      for (let i = 0; i < dataLength; i++) {
        colorPoint = (colorStart + (i * intervalSize));
        colorArray.push(interpolateTurbo(colorPoint));
      }

      return colorArray;
    }
    ,
    cleanVersion(version) {
      // Use a regular expression to detect unwanted trailing letters in the patch part
      return version.replace(/^([\d\\.]+(?:-.+)?)(?:\w.+)?$/, '$1');
    }
  }
}
</script>
