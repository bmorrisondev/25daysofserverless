<template>
  <v-card
      class="mx-2"
      width="350"
      outlined
  >
    <v-list-item two-line>
      <v-list-item-content>
        <h3 style="text-align: left; padding-left: 7px;">{{title}}</h3>
        <v-spacer></v-spacer>
      </v-list-item-content>
    </v-list-item>

    <v-card-actions>
      <v-btn text>Edit</v-btn>
      <v-btn text>Delete</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  props: {
    title: String
  }
}
</script>

<style>

</style>
