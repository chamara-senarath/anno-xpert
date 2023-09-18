// const API_URL = "https://query-interface-api.onrender.com";
const API_URL = "http://127.0.0.1:8000";

export const loadSchema = async (file) => {
    try {
        const formData = new FormData();
        formData.append("file", file);
        formData.append("level", 2);
        const response = await fetch(`${API_URL}/load_schema`, {
            method: "POST",
            body: formData,
        });
        return response.json();
    } catch (e) {
        console.log(e);
        return [];
    }
};

export const loadXml = async (file) => {
    try {
        const formData = new FormData();
        formData.append("file", file);
        const response = await fetch(`${API_URL}/load_xml`, {
            method: "POST",
            body: formData,
        });
        return response.json();
    } catch (e) {
        console.log(e);
        return [];
    }

}

export const getXmlContent = async (filename, query, selectedFilters) => {
    const data = {
        "filename": filename,
        "query": query,
        "filters": selectedFilters,
        "enums": [],
        "is_case_sensitive": "False",
        "fuzzy_level": 8
    }
    try {
        const response = await fetch(`${API_URL}/get_xml_content`, {
            method: "POST",
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data),
        });
        return response.json();
    } catch (e) {
        console.log(e);
        return [];
    }
}