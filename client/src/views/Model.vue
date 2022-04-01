<template>
    <div class="container-fluid">
        Linear Regression Model

        <section class="container">
            <ModelSelect />
        </section>

        <section class="container">
            <ModelForm />
        </section>

        <section class="container mt-4">
            <Results />
        </section>
    </div>
</template>

<script>
import ModelSelect from './../components/ModelSelect.vue'
import ModelForm from './../components/ModelForm.vue'
import Results from './../components/Results.vue'

export default {
    name: 'Model',
    components: { ModelSelect, ModelForm, Results }
}
</script>

<style scoped>

</style>