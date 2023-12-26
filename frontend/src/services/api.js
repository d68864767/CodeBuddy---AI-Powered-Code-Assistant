```javascript
import axios from 'axios';

const API_URL = 'http://localhost:5000';

const generateCode = async (data) => {
    const response = await axios.post(`${API_URL}/generate_code`, data);
    return response.data;
}

const debugCode = async (data) => {
    const response = await axios.post(`${API_URL}/debug_code`, data);
    return response.data;
}

const explainCode = async (data) => {
    const response = await axios.post(`${API_URL}/explain_code`, data);
    return response.data;
}

const generateDoc = async (data) => {
    const response = await axios.post(`${API_URL}/generate_doc`, data);
    return response.data;
}

const learnSupport = async (data) => {
    const response = await axios.post(`${API_URL}/learn_support`, data);
    return response.data;
}

const optimizeCode = async (data) => {
    const response = await axios.post(`${API_URL}/optimize_code`, data);
    return response.data;
}

const storeQuery = async (data) => {
    const response = await axios.post(`${API_URL}/store_query`, data);
    return response.data;
}

export default {
    generateCode,
    debugCode,
    explainCode,
    generateDoc,
    learnSupport,
    optimizeCode,
    storeQuery
};
```
