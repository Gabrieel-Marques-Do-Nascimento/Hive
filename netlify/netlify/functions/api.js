exports.handler = async (event, context) => {
    const API_URL = process.env.API_URL;
    if (!API_URL){ return {statusCode: 500, body: 'API_URL is not defined' };}
    return {
        statusCode: 200,
        body: JSON.stringify({ message: "Olá, backend funcionando no Netlify!", url: API_URL  })
    };
};
