<template>
    <div>
      <upload-file-item></upload-file-item>
    </div>
</template>

<script>
import UploadFileComponent from '@/components/UploadFile';
export default {
  name: 'AdviceManagement',
  components: {
    'upload-file-item': UploadFileComponent,
  },
  data() {
    return {
    };
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>