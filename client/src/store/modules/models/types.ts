export interface ModelState {
    model: string,
    predictedYield: number,
    yieldDiff: number,
    predictedEmergence: number,
    emergenceDiff: number
}
export interface treatmentsParams {
    prep: string,
    pressure: string,
    moisture: string,
    covercrop: string,
    traffic: string
}
export interface treatmentsCompareParams extends treatmentsParams {
    changed_attribute: string
    changed_val: any
}
export interface moistureParams {
    low: number,
    mid: number,
    high: number
}
export interface bdMoistureParams {
    lowMoisture: number,
    midMoisture: number,
    highMoisture: number,
    lowDensity: number,
    midDensity: number,
    highDensity: number
}