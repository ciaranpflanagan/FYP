<template>
    <div class="card">
        <div class="card-body text-center">
            <div class="row">
                <div class="col-md-6 results-text">
                    <span class="var-name">Predicted Yield:</span> <span>{{ predicted_yield }}</span>
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
        predicted_yield () {
            return 0;
        },

        /**
         * Returns predicted emergence from models
         */
        predicted_emergence () {
            return 0;
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