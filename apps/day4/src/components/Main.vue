<template>
  <v-container>
    <v-layout text-center wrap>
      <TaskCard
        v-for="task in tasks"
        v-bind:key="task"
        :title="task.title"
      />

      <!-- <ul>
        <li v-for="task in tasks" v-bind:key="task">{{ task.title }}</li>
      </ul> -->

      <!-- <v-flex xs12>
        <v-card
          class="mx-auto"
          max-width="640"
        >
        <v-list>
          <v-subheader>REPORTS</v-subheader>
          <v-list-item-group v-model="item" color="primary">
            <v-list-item
              v-for="(item, i) in items"
              :key="i"
            >
              <v-list-item-icon>
                <v-icon v-text="item.icon"></v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title v-text="item.text"></v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-item-group>
        </v-list>
        </v-card>
      </v-flex> -->
    </v-layout>
  </v-container>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

// Components
import TaskCard from './TaskCard'

export default {
  name: 'Main',
  components: {
    TaskCard
  },
  computed: {
    ...mapGetters([
      'getTasks'
    ])
  },
  data: () => ({
    tasks: [
      { title: 'this is my thing' },
      { title: 'this is my other thing' }
    ]
  }),
  created: function () {
    // this.fetchTaskData()
  },
  methods: {
    ...mapActions([
      'fetchTaskData'
    ])
  }
}
</script>
