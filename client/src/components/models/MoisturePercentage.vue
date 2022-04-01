<template>
    <div class="card">
        <div class="card-body">
            <form action="" v-on:submit.prevent>
                <div class="row">
                    <div class="col-md-10 offset-md-1">
                        <h3>Moisture Level (Measured in %)</h3>
                        <div class="form-group mb-4">
                            <label><b>Depth:</b> 0 - 10cm</label>
                            <input v-model="low" name="low" type="text" class="form-control">
                        </div>
                        <div class="form-group mb-4">
                            <label><b>Depth:</b> 10 - 20cm</label>
                            <input v-model="mid" name="mid" type="text" class="form-control">
                        </div>
                        <div class="form-group mb-4">
                            <label><b>Depth:</b> 20 - 30cm</label>
                            <input v-model="high" name="high" type="text" class="form-control">
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
    name: 'Moisture Percentage',
    data() {
        return {
            low: 10,
            mid: 20,
            high: 30
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