<template>
    <div class="home">
      <h5><u>With this application User can perform following actions:</u></h5>
      <ul id="about">
        <li>Upload '*.csv' files</li>
        <li>List all the uploaded '*.csv' files as separate documents</li>
        <li>Detailed view of every '*.csv' content in a Table</li>
        <li>Modify the Table view  and store the changes in the '*.csv' along with additional functionality for sorting and searching</li>
        <li>Remove '*.csv' documents from the application</li>
        <li>Enrich selected '*.csv' with external data and created a new '*.csv' record with the result (without changing the original document)</li>
        <li>One OR Two Key Field pairs can do document enrichment</li>
      </ul>
    </div>
</template>

<script>
export default {
  name: 'AboutPage',
  props: {}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#about li {
    list-style-type: none;
}
</style>