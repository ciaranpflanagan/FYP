import { RootState } from "@/store/types";
import { ActionTree } from "vuex";
import { ModelState } from "./types";

interface params {
    prep: string,
    pressure: string,
    moisture: string,
    covercrop: string,
    traffic: string
}

export const actions: ActionTree<ModelState, RootState> = {
    loadTreatments ({ commit }, payload: params): any {
        console.log('payload', payload);
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
            console.log('loadTreatments return', data);
            
            commit('setTreatments', data);
            return data;
        });
    }
}