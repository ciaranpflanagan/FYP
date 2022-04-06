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

        // Resetting differences
        state.yieldDiff = 0;
        state.emergenceDiff = 0;
    },

    /**
     * Sets predicted values from models and their difference
     * @param state 
     * @param payload 
     */
    setComparisonResults(state, payload) {
        state.predictedYield = payload.yield.result;
        state.predictedEmergence = payload.emergence.result;

        // Resetting differences
        state.yieldDiff = payload.yield.difference;
        state.emergenceDiff = payload.emergence.difference;
    },

    /**
     * Sets the currently selected model
     * @param state 
     * @param payload 
     */
    updateSelectedModel(state, payload) {
        state.model = payload; // Update model

        // Resetting results when model changed
        state.predictedYield = 0;
        state.predictedEmergence = 0;
    }
}