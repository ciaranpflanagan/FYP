<template>
    <div class="card">
        <div class="card-body">
            <form action="" v-on:submit.prevent>
                <div class="row">
                    <div class="col-md-5 offset-md-1">
                        <h3>Moisture Level (Measured in %)</h3>
                        <div class="form-group mb-4">
                            <label><b>Depth:</b> 0 - 10cm</label>
                            <input v-model="lowMoisture" name="low_moisture" type="text" class="form-control">
                        </div>
                        <div class="form-group mb-4">
                            <label><b>Depth:</b> 10 - 20cm</label>
                            <input v-model="midMoisture" name="mid_moisture" type="text" class="form-control">
                        </div>
                        <div class="form-group mb-4">
                            <label><b>Depth:</b> 20 - 30cm</label>
                            <input v-model="highMoisture" name="high_moisture" type="text" class="form-control">
                        </div>
                    </div>
                    <div class="col-md-5">
                        <h3>Density (Measured in gcm^3)</h3>
                        <div class="form-group mb-4">
                            <label><b>Depth:</b> 0 - 10cm</label>
                            <input v-model="lowDensity" name="low_density" type="text" class="form-control">
                        </div>
                        <div class="form-group mb-4">
                            <label><b>Depth:</b> 10 - 20cm</label>
                            <input v-model="midDensity" name="mid_density" type="text" class="form-control">
                        </div>
                        <div class="form-group mb-4">
                            <label><b>Depth:</b> 20 - 30cm</label>
                            <input v-model="highDensity" name="high_density" type="text" class="form-control">
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-6 offset-md-3">
                        <button @click="submit()" type="submit" class="btn btn-primary" style="width: 100%;" >Submit</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
export default {
    name: 'BDMoisture',
    data() {
        return {
            lowMoisture: 10,
            midMoisture: 20,
            highMoisture: 30,
            lowDensity: 10,
            midDensity: 20,
            highDensity: 30,
        }
    },
    methods: {
        /**
         * Dispatches vuex action to get data from models
         */
        submit() {
            this.$store.dispatch('loadMoisturePercentage', {
                low: this.low,
                mid: this.mid,
                high: this.high,
            });
        }
    }
}
</script>

<style>

</style>