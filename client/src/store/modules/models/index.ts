import { Module } from 'vuex'
import { RootState } from '@/store/types'
import { actions } from './actions'
import { mutations } from './mutations'
import { ModelState } from './types'

const state: ModelState = {
    model: "treatments", // default model is "treatments"
    predictedYield: 0,
    predictedEmergence: 0
}

export const models: Module<ModelState, RootState> = {
    state,
    actions,
    mutations
}