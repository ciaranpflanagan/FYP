<template>
    <div class="container-fluid mt-4">
        <section class="container">
            <ModelSelect />
        </section>

        <section class="container">
            <Treatments v-if="model === 'treatments'" />
            <TreatmentsMoisture v-if="model === 'treatments_moisture'" />
            <MoisturePercentage v-if="model === 'moisture_percentage'" />
            <BDMoisture v-if="model === 'bd_moisture'" />
        </section>

        <section class="container mt-4">
            <Results />
        </section>
    </div>
</template>

<script>
import ModelSelect from './../components/ModelSelect.vue'
import Treatments from './../components/models/Treatments.vue'
import TreatmentsMoisture from './../components/models/TreatmentsMoisture.vue'
import MoisturePercentage from './../components/models/MoisturePercentage.vue'
import BDMoisture from './../components/models/BDMoisture.vue'
import Results from './../components/Results.vue'

export default {
    name: 'Model',
    components: { ModelSelect, Treatments, TreatmentsMoisture, MoisturePercentage, BDMoisture, Results },
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