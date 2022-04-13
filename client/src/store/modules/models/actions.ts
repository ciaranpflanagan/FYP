import { RootState } from "@/store/types";
import { ActionTree } from "vuex";
import * as types from "./types";

export const actions: ActionTree<types.ModelState, RootState> = {
    /**
     * Loads results from treatment models based on data passed
     * @param payload 
     * @returns 
     */
    loadTreatments ({ commit }, payload: types.treatmentsParams): any {
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
     * Loads compared results from treatment models
     * @param payload 
     * @returns 
     */
    loadCompareTreatments ({ commit }, payload: types.treatmentsCompareParams): any {
        const formData = new FormData();

        formData.append('prep', payload.prep);
        formData.append('pressure', payload.pressure);
        formData.append('moisture', payload.moisture);
        formData.append('covercrop', payload.covercrop);
        formData.append('traffic', payload.traffic);
        formData.append('changed_attribute', payload.changed_attribute);
        formData.append('changed_val', payload.changed_val);
        
        return fetch('http://127.0.0.1:5001/treatments/compare', {
            method: 'POST',
            body: formData
        }).then(data => data.json()).then(data => {
            console.log('loadCompareTreatments', data);
            
            commit('setComparisonResults', data);
            return data;
        });
    },

    /**
     * Loads results from treatment granular moisture models
     * @param payload 
     * @returns 
     */
    loadTreatmentsMoisture ({ commit }, payload: types.treatmentsParams): any {
        const formData = new FormData();

        formData.append('prep', payload.prep);
        formData.append('pressure', payload.pressure);
        formData.append('moisture', payload.moisture);
        formData.append('covercrop', payload.covercrop);
        formData.append('traffic', payload.traffic);
        
        return fetch('http://127.0.0.1:5001/treatments-moisture', {
            method: 'POST',
            body: formData
        }).then(data => data.json()).then(data => {
            console.log('loadTreatmentsMoisture', data);
            
            commit('setResults', data);
            return data;
        });
    },

    /**
     * Loads compared results from treatment granular moisture models
     * @param payload 
     * @returns 
     */
    loadCompareTreatmentsMoisture ({ commit }, payload: types.treatmentsCompareParams): any {
        const formData = new FormData();

        formData.append('prep', payload.prep);
        formData.append('pressure', payload.pressure);
        formData.append('moisture', payload.moisture);
        formData.append('covercrop', payload.covercrop);
        formData.append('traffic', payload.traffic);
        formData.append('changed_attribute', payload.changed_attribute);
        formData.append('changed_val', payload.changed_val);
        
        return fetch('http://127.0.0.1:5001/treatments-moisture/compare', {
            method: 'POST',
            body: formData
        }).then(data => data.json()).then(data => {
            console.log('loadCompareTreatmentsMoisture', data);
            
            commit('setComparisonResults', data);
            return data;
        });
    },

    /**
     * Loads results from moisture % models based on data passed
     * @param payload 
     * @returns 
     */
    loadMoisturePercentage ({ commit }, payload: types.moistureParams): any {
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
    loadBDMoisture ({ commit }, payload: types.bdMoistureParams): any {
        const formData = new FormData();

        formData.append('lowMoisture', JSON.stringify(payload.lowMoisture));
        formData.append('midMoisture', JSON.stringify(payload.midMoisture));
        formData.append('highMoisture', JSON.stringify(payload.highMoisture));
        formData.append('lowDensity', JSON.stringify(payload.lowDensity));
        formData.append('midDensity', JSON.stringify(payload.midDensity));
        formData.append('highDensity', JSON.stringify(payload.highDensity));
        
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