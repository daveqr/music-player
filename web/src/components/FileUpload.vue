<script setup>
import { ref } from 'vue';

const fileInput = ref(null);

const uploadFile = async () => {
    const file = fileInput.value.files[0];

    if (!file) {
        return;
    }

    const formData = new FormData();
    formData.append('file_uploaded', file);

    console.log('uploading file')
    try {
        const response = await fetch('http://localhost:8000/upload/', {
            method: 'POST',
            body: formData,
        });

        if (response.ok) {
            console.log('File uploaded successfully');
        } else {
            console.error('File upload failed');
        }
    } catch (error) {
        console.error('Error uploading file:', error);
    }
}
</script>

<template>
    <div>
        <input type="file" ref="fileInput" @change="uploadFile" />
    </div>
</template>
  