import { MutationTree } from "vuex";
import { ModelState } from "./types";

export const mutations: MutationTree<ModelState> = {
    /**
     * Sets predicted values from models
     * @param state 
     * @param payload 
     */
    setResults(state, payload) {
        state.yield.result = payload.yield.result;
        state.emergence.result = payload.emergence.result;

        // Resetting differences
        state.yield.diff = 0;
        state.emergence.diff = 0;
    },

    /**
     * Sets predicted values from models and their difference
     * @param state 
     * @param payload 
     */
    setComparisonResults(state, payload) {
        state.yield.result = payload.yield.result;
        state.yield.result2 = payload.yield.result2;
        state.emergence.result = payload.emergence.result;
        state.emergence.result2 = payload.emergence.result2;

        // Resetting differences
        state.yield.diff = payload.yield.difference;
        state.emergence.diff = payload.emergence.difference;
    },

    /**
     * Sets the currently selected model
     * @param state 
     * @param payload 
     */
    updateSelectedModel(state, payload) {
        state.model = payload; // Update model

        // Resetting results when model changed
        state.yield.result = 0;
        state.yield.result2 = 0;
        state.yield.diff = 0;

        state.emergence.result = 0;
        state.emergence.result2 = 0;
        state.emergence.diff = 0;
    },

    /**
     * Resets predictions
     * @param state
     */
    resetPredictions(state) {
        state.yield.result = 0;
        state.yield.result2 = 0;
        state.yield.diff = 0;

        state.emergence.result = 0;
        state.emergence.result2 = 0;
        state.emergence.diff = 0;
    }
}