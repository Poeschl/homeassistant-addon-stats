<template>
  <div class="card">
    <div class="card-body">
      <h5 class="card-title">Latest installations grouped by version</h5>
      <div class="chart-container">
        <Doughnut :data="chartData" :options="chartOptions"/>
      </div>
    </div>
  </div>
</template>

<script>
import {Doughnut} from 'vue-chartjs';
import {ArcElement, Chart as ChartJS, Legend, Tooltip} from 'chart.js'
import {interpolateTurbo} from "d3-scale-chromatic";
import {compareVersions} from "compare-versions";

ChartJS.register(ArcElement, Tooltip, Legend);

export default {
  name: "VersionsChart",
  props: ["versions"],
  components: {
    Doughnut
  },
  data() {
    return {
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
        borderColor: '#121213',
        plugins: {
          legend: {
            position: 'right'
          }
        }
      }
    }
  },
  computed: {
    chartData() {
      if (this.versions === undefined || this.versions.length === 0) {
        return {
          labels: [],
          datasets: []
        }
      }

      const sortedVersions = Object.keys(this.versions).map((key) => {
        return [key, this.versions[key]]
      }).sort((first, second) => {
        const cleanedFirst = this.cleanVersion(first[0])
        const cleanedSecond = this.cleanVersion(second[0])
        return compareVersions(cleanedFirst, cleanedSecond)
      })

      const labels = []
      const values = []
      for (const versionData of sortedVersions) {
        labels.push(versionData[0])
        values.push(versionData[1])
      }
      const colors = this.generateColors(labels.length)

      return {
        labels: labels,
        datasets: [
          {
            backgroundColor: colors,
            data: values
          }
        ]
      }
    }
  },
  methods: {
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
    },
    cleanVersion(version) {
      // Use a regular expression to detect unwanted trailing letters in the patch part
      return version.replace(/^([\d\\.]+(?:-.+)?)(?:\w.+)?$/, '$1');
    }
  }
}
</script>
