import { MutationTree } from "vuex";
import { ModelState } from "./types";

export const mutations: MutationTree<ModelState> = {
    /**
     * Sets predicted values from models
     * @param state 
     * @param payload 
     */
    setResults(state, payload) {
        state.predictedYield = payload.yield;
        state.predictedEmergence = payload.emergence;
    },

    /**
     * Sets the currently selected model
     * @param state 
     * @param payload 
     */
    updateSelectedModel(state, payload) {
        state.model = payload
    }
}