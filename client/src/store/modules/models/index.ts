import { Module } from 'vuex'
import { RootState } from '@/store/types'
import { actions } from './actions'
import { mutations } from './mutations'
import { ModelState } from './types'

const state: ModelState = {
    model: "treatments", // default model is "treatments"
    yield: {
        result: 0,
        result2: 0,
        diff: 0
    },
    emergence: {
        result: 0,
        result2: 0,
        diff: 0
    }
}

export const models: Module<ModelState, RootState> = {
    state,
    actions,
    mutations
}