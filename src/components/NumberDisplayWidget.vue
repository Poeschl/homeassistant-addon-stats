<template>
  <div class="card">
    <div class="card-body row">
      <div class="col" v-for="data in this.values" :key="data">
        <div class="d-flex flex-column justify-content-evenly align-items-center h-100">
          <span class="h5">{{ data.title }}</span>
          <span>{{ data.value }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "NumberDisplayWidget",
  props: ["values"]
}
</script>

<style scoped>

</style>
