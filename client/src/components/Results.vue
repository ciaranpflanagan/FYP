<template>
    <div class="card">
        <div class="card-body text-center">
            <div class="row">
                <div class="col-md-6 results-text">
                    <span class="var-name">Predicted Yield:</span> <span>{{ predicted_yield }} t/ac</span>
                </div>
                <div class="col-md-6 results-text">
                    <span class="var-name">Predicted Emergence:</span> <span>{{ predicted_emergence }}</span>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Results',
    computed: {
        /**
         * Returns predicted yield from models
         */
        predicted_yield() {
            // console.log(this.$store.state.models);
            let predictedYield = this.$store.state.models.yield.result;

            return (predictedYield === 0) ? 0 : predictedYield.toPrecision(6);
        },

        /**
         * Returns predicted emergence from models
         */
        predicted_emergence () {
            let emergence = this.$store.state.models.emergence.result;

            return (emergence === 0) ? 0 : emergence.toPrecision(6);
        }
    }
}
</script>

<style scoped>
    .var-name {
        font-weight: 700;
    }
    .results-text {
        font-size: 2em;
    }
</style>