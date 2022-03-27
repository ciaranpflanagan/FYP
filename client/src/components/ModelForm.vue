<template>
    <div class="card">
        <div class="card-body">
            <form action="">
                <div class="row">
                    <div class="col-md-2 offset-md-1">
                        <div class="form-group mb-4">
                            <label>Soil Preparation</label>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" value="ploughed" name="prep" id="ploughed_prep" checked>
                                <label class="form-check-label" for="ploughed_prep">
                                    Ploughed
                                </label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" value="tilled" name="prep" id="tilled_prep">
                                <label class="form-check-label" for="tilled_prep">
                                    Tilled
                                </label>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-2">
                        <div class="form-group mb-4">
                            <label>Pressure</label>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" value="high" name="pressure" id="high_pressure" checked>
                                <label class="form-check-label" for="high_pressure">
                                    High
                                </label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" value="low" name="pressure" id="low_pressure">
                                <label class="form-check-label" for="low_pressure">
                                    Low
                                </label>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-2">
                        <div class="form-group mb-4">
                            <label>Moisture Level</label>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" value="high" name="moisture" id="high_moisture" checked>
                                <label class="form-check-label" for="high_moisture">
                                    High
                                </label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" value="low" name="moisture" id="low_moisture">
                                <label class="form-check-label" for="low_moisture">
                                    Low
                                </label>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-2">
                        <div class="form-group mb-4">
                            <label>Covercrop</label>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" value="yes" name="covercrop" id="yes_covercrop" checked>
                                <label class="form-check-label" for="yes_covercrop">
                                    Yes
                                </label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" value="no" name="covercrop" id="no_covercrop">
                                <label class="form-check-label" for="no_covercrop">
                                    No
                                </label>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-2">
                        <div class="form-group mb-4">
                            <label>Traffic Level</label>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" value="high" name="traffic" id="high_traffic" checked>
                                <label class="form-check-label" for="high_traffic">
                                    High
                                </label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" value="low" name="traffic" id="low_traffic">
                                <label class="form-check-label" for="low_traffic">
                                    Low
                                </label>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-6 offset-md-3">
                        <button type="submit" class="btn btn-primary" style="width: 100%;">Submit</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ModelForm'
}
</script>

<style scoped>

</style>