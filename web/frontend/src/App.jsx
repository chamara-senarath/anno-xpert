import { useState } from "react";
import { getXmlContent, loadSchema, loadXml } from "./api";
import { HierarchyDropdowns } from "./HierarchyDropdowns";
import SearchSection from "./SearchSection";
import { useEffect } from "react";
import ResultView from "./ResultView";
import Filters from "./Filters";
import { joinArraysWithoutDuplicates } from "./helpers";

function App() {
  const [dropdownValues, setDropDownValues] = useState({});
  const [selectedDropdowns, setSelectedDropdowns] = useState({});
  const [xmlID, setXmlID] = useState("");
  const [results, setResults] = useState([]);
  const [query, setQuery] = useState("");
  const [matchLevel, setMatchLevel] = useState(8);
  const [isCaseSensitive, setIsCaseSensitive] = useState(false);
  const [selectedFilters, setSelectedFilters] = useState([]);
  const [enums, setEnums] = useState({});

  useEffect(() => {
    if (localStorage.getItem("fileID")) {
      setXmlID(localStorage.getItem("fileID"));
    }
  }, []);

  useEffect(() => {
    if (xmlID) {
      localStorage.setItem("fileID", xmlID);
    }
  }, [xmlID]);

  useEffect(() => {
    fetchXmlContent();
  }, [
    selectedFilters,
    query,
    matchLevel,
    isCaseSensitive,
    enums,
    selectedDropdowns,
  ]);

  const handleLoadSchema = async (file) => {
    const data = await loadSchema(file);
    if (data.data) {
      setDropDownValues(data.data);
    }
  };

  const handleLoadData = async (file) => {
    const data = await loadXml(file);
    if (data.filename) {
      setXmlID(data.filename);
    }
  };

  const handleChangeDropdowns = (level, value, isEnumeration) => {
    setSelectedFilters([]);
    if (isEnumeration) {
      setEnums((prev) => {
        return {
          ...prev,
          [level - 1]: {
            parent: selectedDropdowns[level - 1],
            enum: value,
          },
        };
      });
    } else {
      const selected = {
        ...selectedDropdowns,
        [level]: value,
      };
      setSelectedDropdowns(
        Object.fromEntries(
          Object.entries(selected).filter(([k, _]) => k <= level)
        )
      );
      setEnums(
        Object.fromEntries(
          Object.entries(enums).filter(([k, _]) => k.parent <= level - 1)
        )
      );
    }
  };

  const handleSearch = async (query, matchLevel, isCaseSensitive) => {
    setQuery(query);
    setMatchLevel(matchLevel);
    setIsCaseSensitive(isCaseSensitive);
  };

  const fetchXmlContent = async () => {
    if (!xmlID) return;
    const data = await getXmlContent(
      xmlID,
      query,
      joinArraysWithoutDuplicates(
        Object.values(selectedDropdowns),
        selectedFilters
      ),
      matchLevel,
      Object.values(enums),
      isCaseSensitive
    );
    if (data.value) {
      setResults(data.value);
    }
  };

  const handleOnSelectFilter = (filter) => {
    if (selectedFilters.includes(filter)) {
      setSelectedFilters(selectedFilters.filter((f) => f !== filter));
    } else {
      setSelectedFilters([...selectedFilters, filter]);
    }
  };

  const clearSelectedFilters = () => {
    setSelectedFilters([]);
  };

  const clearDropdowns = () => {
    setSelectedDropdowns({});
    setEnums({});
  }

  return (
    <>
      <div className="navbar bg-base-100 px-12">
        <div className="flex-1">
          <span className="text-2xl font-bold">AnnoXpert</span>
        </div>
        <div className="flex-none space-x-4">
          <div className="relative">
            <a className="btn btn-sm btn-primary">
              <span>Load Schema</span>
              <input
                type="file"
                className="opacity-0 absolute w-28"
                onChange={(e) => {
                  handleLoadSchema(e.target.files[0]);
                }}
              />
            </a>
          </div>
          <div className="relative">
            <a className="btn btn-sm btn-primary">
              <span>Load Data</span>
              <input
                type="file"
                className="opacity-0 absolute w-28"
                onChange={(e) => {
                  handleLoadData(e.target.files[0]);
                }}
              />
            </a>
          </div>
        </div>
      </div>

      <div className="flex flex-col px-12 space-y-4">
        {dropdownValues && Object.keys(dropdownValues).length > 0 && (
          <div className="flex space-x-4">
            <HierarchyDropdowns
              data={dropdownValues}
              onChange={handleChangeDropdowns}
              selected={selectedDropdowns}
            />
            <button className="btn btn-neutral btn-outline" onClick={clearDropdowns}>
              Clear Dropdowns
            </button>
          </div>
        )}

        <SearchSection onSearch={handleSearch} />
        {results.length > 0 && (
          <div className="flex space-x-4">
            <ResultView results={results} />
            <Filters
              results={results}
              onSelect={handleOnSelectFilter}
              selected={selectedFilters}
              clear={clearSelectedFilters}
            />
          </div>
        )}
      </div>
    </>
  );
}

export default App;
