<template>
    <div class="card">
        <div class="card-body">
            <form action="" v-on:submit.prevent>
                <div class="row mb-2" style="text-align: center;">
                    <h3>Soil Treatments</h3>
                </div>
                <div class="row">
                    <div class="col-md-2 offset-md-1">
                        <div class="form-group mb-4">
                            <label>Soil Preparation</label>
                            <div class="form-check">
                                <input v-model="prep" class="form-check-input" type="radio" value="ploughed" name="prep" id="ploughed_prep">
                                <label class="form-check-label" for="ploughed_prep">
                                    Ploughed
                                </label>
                            </div>
                            <div class="form-check">
                                <input v-model="prep" class="form-check-input" type="radio" value="tilled" name="prep" id="tilled_prep">
                                <label class="form-check-label" for="tilled_prep">
                                    Tilled
                                </label>
                            </div>

                            <!-- Compare Checkbox -->
                            <div class="form-check compare-attribute mt-2">
                                <input v-model="comparedAttVal" class="form-check-input" type="radio" value="prep" id="compareVal">
                                <label class="form-check-label" for="comparePrepCheck">
                                    Compare?
                                </label>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-2">
                        <div class="form-group mb-4">
                            <label>Pressure</label>
                            <div class="form-check">
                                <input v-model="pressure" class="form-check-input" type="radio" value="high" name="pressure" id="high_pressure">
                                <label class="form-check-label" for="high_pressure">
                                    High
                                </label>
                            </div>
                            <div class="form-check">
                                <input v-model="pressure" class="form-check-input" type="radio" value="low" name="pressure" id="low_pressure">
                                <label class="form-check-label" for="low_pressure">
                                    Low
                                </label>
                            </div>

                            <!-- Compare Checkbox -->
                            <div class="form-check compare-attribute mt-2">
                                <input v-model="comparedAttVal" class="form-check-input" type="radio" value="pressure" id="compareVal">
                                <label class="form-check-label" for="comparePressureCheck">
                                    Compare?
                                </label>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-2">
                        <div class="form-group mb-4">
                            <label>Moisture Level</label>
                            <div class="form-check">
                                <input v-model="moisture" class="form-check-input" type="radio" value="high" name="moisture" id="high_moisture">
                                <label class="form-check-label" for="high_moisture">
                                    High
                                </label>
                            </div>
                            <div class="form-check">
                                <input v-model="moisture" class="form-check-input" type="radio" value="low" name="moisture" id="low_moisture">
                                <label class="form-check-label" for="low_moisture">
                                    Low
                                </label>
                            </div>

                            <!-- Compare Checkbox -->
                            <div class="form-check compare-attribute mt-2">
                                <input v-model="comparedAttVal" class="form-check-input" type="radio" value="moisture" id="compareVal">
                                <label class="form-check-label" for="comparePressureCheck">
                                    Compare?
                                </label>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-2">
                        <div class="form-group mb-4">
                            <label>Covercrop</label>
                            <div class="form-check">
                                <input v-model="covercrop" class="form-check-input" type="radio" value="yes" name="covercrop" id="yes_covercrop">
                                <label class="form-check-label" for="yes_covercrop">
                                    Yes
                                </label>
                            </div>
                            <div class="form-check">
                                <input v-model="covercrop" class="form-check-input" type="radio" value="no" name="covercrop" id="no_covercrop">
                                <label class="form-check-label" for="no_covercrop">
                                    No
                                </label>
                            </div>

                            <!-- Compare Checkbox -->
                            <div class="form-check compare-attribute mt-2">
                                <input v-model="comparedAttVal" class="form-check-input" type="radio" value="covercrop" id="compareVal">
                                <label class="form-check-label" for="comparePressureCheck">
                                    Compare?
                                </label>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-2">
                        <div class="form-group mb-4">
                            <label>Traffic Level</label>
                            <div class="form-check">
                                <input v-model="traffic" class="form-check-input" type="radio" value="high" name="traffic" id="high_traffic">
                                <label class="form-check-label" for="high_traffic">
                                    High
                                </label>
                            </div>
                            <div class="form-check">
                                <input v-model="traffic" class="form-check-input" type="radio" value="low" name="traffic" id="low_traffic">
                                <label class="form-check-label" for="low_traffic">
                                    Low
                                </label>
                            </div>

                            <!-- Compare Checkbox -->
                            <div class="form-check compare-attribute mt-2">
                                <input v-model="comparedAttVal" class="form-check-input" type="radio" value="traffic" id="compareVal">
                                <label class="form-check-label" for="comparePressureCheck">
                                    Compare?
                                </label>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-3 offset-md-3">
                        <button @click="submit()" type="submit" class="btn btn-primary" style="width: 100%;">Submit</button>
                    </div>
                    <div class="col-md-3">
                        <button @click="reset()" type="submit" class="btn btn-danger" style="width: 100%;">Reset</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Treatments',
    data() {
        return {
            prep: 'ploughed',
            pressure: 'high',
            moisture: 'high',
            covercrop: 'no',
            traffic: 'high',
            comparedAttVal: null
        }
    },
    methods: {
        /**
         * Dispatches vuex action to get data from models
         */
        submit() {
            if (this.comparedAttVal === null) {
                this.$store.dispatch('loadTreatments', {
                    prep: this.prep,
                    pressure: this.pressure,
                    moisture: this.moisture,
                    covercrop: this.covercrop,
                    traffic: this.traffic
                });
            } else {
                this.$store.dispatch('loadCompareTreatments', {
                    prep: this.prep,
                    pressure: this.pressure,
                    moisture: this.moisture,
                    covercrop: this.covercrop,
                    traffic: this.traffic,
                    changed_attribute: this.comparedAttVal,
                    changed_val: this.getComparisonVal()
                });
            }
        },

        /**
         * Returns the compared value, opposite value in binary attribute
         */
        getComparisonVal() {
            switch (this.comparedAttVal) {
                case 'prep':
                    return (this.prep === 'ploughed') ? 'tilled' : 'ploughed';
                case 'pressure':
                    return (this.pressure === 'high') ? 'low' : 'high';
                case 'moisture':
                    return (this.moisture === 'high') ? 'low' : 'high';
                case 'covercrop':
                    return (this.covercrop === 'no') ? 'yes' : 'no';
                case 'traffic':
                    return (this.traffic === 'high') ? 'low' : 'high';
            }
        },

        /**
         * Resets predictions
         */
        reset() {
            this.$store.commit('resetPredictions');
        }
    }
}
</script>

<style computed>
.compare-attribute {
    font-size: .8em;
    color: #0d6efd;
    font-weight: 600;
    cursor: pointer;
}
</style>