<template>
    <div class="card mb-4">
        <div class="card-body">
            <div class="row">
                <div class="col-md-10 offset-md-1">
                    <div class="form-group">
                        <label for="model_name mb-2">Select Model</label>
                        <select v-model="modelName" name="model_name" class="form-control">
                            <option v-for="model in models" :key="model.id" :value="model.model">{{ model.name }}</option>
                        </select>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ModelSelect',
    data() {
        return {
            models: [
                {id: 1, name: 'Bulk Density & Moisture', model: 'bd_moisture'},
                {id: 2, name: 'Moisture Percentage', model: 'moisture_percentage'},
                {id: 3, name: 'Soil Treatments', model: 'treatments'}
            ]
        }
    },
    computed: {
        modelName: {
            get() {
                return this.$store.state.models.model;
            },
            set(val) {
                this.$store.commit('updateSelectedModel', val);
            }
        }
    }
}
</script>

<style>

</style>