import { createStore } from 'vuex'

import { models } from './modules/models'

export default createStore({
	modules: {
		models
	}
})
