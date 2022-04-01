<template>
    <div class="container-fluid">
        Linear Regression Model

        <section class="container">
            <ModelSelect />
        </section>

        <section class="container">
            <BDMoisture v-if="model === 'bd_moisture'" />
            <MoisturePercentage v-if="model === 'moisture_percentage'" />
            <Treatments v-if="model === 'treatments'" />
        </section>

        <section class="container mt-4">
            <Results />
        </section>
    </div>
</template>

<script>
import ModelSelect from './../components/ModelSelect.vue'
import BDMoisture from './../components/models/BDMoisture.vue'
import MoisturePercentage from './../components/models/MoisturePercentage.vue'
import Treatments from './../components/models/Treatments.vue'
import Results from './../components/Results.vue'

export default {
    name: 'Model',
    components: { ModelSelect, BDMoisture, MoisturePercentage, Treatments, Results },
    computed: {
        /**
         * Returns the current active model
         */
        model() {
            return this.$store.state.models.model;
        }
    }
}
</script>

<style scoped>

</style>