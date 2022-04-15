<template>
    <div class="card">
        <div class="card-body text-center">
            <div class="row">
                <div class="col-md-6 results-text">
                    <span class="var-name">Predicted Yield:</span> <span>{{ predicted_yield }} t/ac</span>
                    <br>
                    <div v-if="yield_difference != 0">
                        <span class="compared-name">Compared Yield:</span> <span>{{ predicted_second_yield }} t/ac</span>
                        <br>
                        <span class="difference-text">Difference:</span>&nbsp;
                        <span :class="(yield_difference < 0) ? 'difference-val-negative' : 'difference-val-positive'">
                            {{ yield_difference }} %
                        </span>
                    </div>
                </div>
                <div class="col-md-6 results-text">
                    <span class="var-name">Predicted Emergence:</span> <span>{{ predicted_emergence }}</span>
                    <br>
                    <div v-if="emergence_difference != 0">
                        <span class="compared-name">Compared Yield:</span> <span>{{ predicted_second_emergence }} t/ac</span>
                        <br>
                        <span class="difference-text">Difference:</span>&nbsp;
                        <span :class="(emergence_difference < 0) ? 'difference-val-negative' : 'difference-val-positive'">
                            {{ emergence_difference }} %
                        </span>
                    </div>
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
            let predictedYield = this.$store.state.models.yield.result;

            return (predictedYield === 0) ? 0 : predictedYield.toPrecision(6);
        },

        /**
         * Returns the second predicted yield from models
         */
        predicted_second_yield() {
            let predictedYield = this.$store.state.models.yield.result2;

            return (predictedYield === 0) ? 0 : predictedYield.toPrecision(6);
        },

        /**
         * Returns predicted emergence from models
         */
        predicted_emergence () {
            let emergence = this.$store.state.models.emergence.result;

            return (emergence === 0) ? 0 : emergence.toPrecision(6);
        },

        /**
         * Returns the second predicted emergence from models
         */
        predicted_second_emergence () {
            let emergence = this.$store.state.models.emergence.result2;

            return (emergence === 0) ? 0 : emergence.toPrecision(6);
        },

        /**
         * Returns difference in yields rounded to 4 numbers
         */
        yield_difference () {
            return this.$store.state.models.yield.diff.toPrecision(4);
        },

        /**
         * Returns difference in emergence rounded to 4 numbers
         */
        emergence_difference () {
            return this.$store.state.models.emergence.diff.toPrecision(4);
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
    .results-text > .compared-name {
        font-style: italic;
        font-weight: 500;
    }
    .results-text .difference-val-positive {
        color: #0dc305;
    }
    .results-text .difference-val-negative {
        color: #c60101;
    }
</style>