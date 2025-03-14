const axios = require('axios');

exports.handler = async (event, context) => {
    const API_KEY = process.env.API_KEY;
    const API_URL = process.env.API_URL;
    //if (!API_KEY){ return {{ statusCode: 500, body: 'API_KEY is not defined' };}}}
    const path  = event.path.replace('/.netlify/functions/api-proxy', '');
    const queyString = event.queryStringParameters ? new URLSearchParams(event.queryStringParameters).toString() : '';
    const url = `${API_URL}${path}?${queyString ? '?' + queyString : ''}`;
    const header = {
        'Content-Type': 'application/json',
        //'Authorization': `Bearer ${API_KEY}`
    }
}