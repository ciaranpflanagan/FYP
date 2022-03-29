import { MutationTree } from "vuex";
import { ModelState } from "./types";

export const mutations: MutationTree<ModelState> = {
    /**
     * Sets predicted values from models
     * @param state 
     * @param payload 
     */
    setTreatments(state, payload) {
        state.predictedYield = payload.yield;
        state.predictedEmergence = payload.emergence;
    }
}