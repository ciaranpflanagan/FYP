import { RootState } from "@/store/types";
import { ActionTree } from "vuex";
import { ModelState } from "./types";

interface treatmentsParams {
    prep: string,
    pressure: string,
    moisture: string,
    covercrop: string,
    traffic: string
}
interface moistureParams {
    low: number,
    mid: number,
    high: number
}
interface bdMoistureParams {
    lowMoisture: number,
    midMoisture: number,
    highMoisture: number,
    lowDensity: number,
    midDensity: number,
    highDensity: number
}

export const actions: ActionTree<ModelState, RootState> = {
    /**
     * Loads results from treatment models based on data passed
     * @param payload 
     * @returns 
     */
    loadTreatments ({ commit }, payload: treatmentsParams): any {
        const formData = new FormData();

        formData.append('prep', payload.prep);
        formData.append('pressure', payload.pressure);
        formData.append('moisture', payload.moisture);
        formData.append('covercrop', payload.covercrop);
        formData.append('traffic', payload.traffic);
        
        return fetch('http://127.0.0.1:5001/treatments', {
            method: 'POST',
            body: formData
        }).then(data => data.json()).then(data => {
            console.log('loadTreatments', data);
            
            commit('setResults', data);
            return data;
        });
    },

    /**
     * Loads results from moisture % models based on data passed
     * @param payload 
     * @returns 
     */
    loadMoisturePercentage ({ commit }, payload: moistureParams): any {
        const formData = new FormData();

        formData.append('low', JSON.stringify(payload.low));
        formData.append('mid', JSON.stringify(payload.mid));
        formData.append('high', JSON.stringify(payload.high));
        
        return fetch('http://127.0.0.1:5001/moisture-precentage', {
            method: 'POST',
            body: formData
        }).then(data => data.json()).then(data => {
            console.log('loadMoisturePercentage', data);
            
            commit('setResults', data);
            return data;
        });
    },

    /**
     * Loads results from the combined bulk density and soil moisture models based on data passed
     * @param payload 
     * @returns 
     */
    loadBDMoisture ({ commit }, payload: bdMoistureParams): any {
        const formData = new FormData();

        formData.append('lowMoisture', JSON.stringify(payload.low));
        formData.append('midMoisture', JSON.stringify(payload.mid));
        formData.append('highMoisture', JSON.stringify(payload.high));
        formData.append('lowDensity', JSON.stringify(payload.low));
        formData.append('midDensity', JSON.stringify(payload.mid));
        formData.append('highDensity', JSON.stringify(payload.high));
        
        return fetch('http://127.0.0.1:5001/bd-moisture', {
            method: 'POST',
            body: formData
        }).then(data => data.json()).then(data => {
            console.log('loadBDMoisture', data);
            
            commit('setResults', data);
            return data;
        });
    }
}