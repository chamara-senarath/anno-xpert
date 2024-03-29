const API_URL = "https://ill-pink-duck-wear.cyclic.cloud";

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

export const getXmlContent = async (filename, query, selectedFilters, matchLevel, enums, isCaseSensitive) => {
    const data = {
        "filename": filename,
        "query": query,
        "filters": selectedFilters,
        "enums": enums,
        "fuzzy_level": matchLevel,
        "is_case_sensitive": isCaseSensitive,
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