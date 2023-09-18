export const HierarchyDropdowns = ({ data, onChange, selected }) => {
  const handleChange = (level, value) => {
    onChange(level, value);
  };

  return (
    <div className="flex space-x-4 ">
      {/* Parent - Level 1 */}
      {Object.keys(data).length > 0 && (
        <select
          className="select select-primary"
          onChange={(e) => handleChange("level1", e.target.value)}
        >
          {Object.keys(data).map((value, index) => (
            <option value={value} key={index}>
              {value}
            </option>
          ))}
        </select>
      )}

      {/* Enumeration - Level 2 */}
      {selected["level1"] && data[selected["level1"]]?.enumerations && (
        <select
          className="select select-accent"
          onChange={(e) => handleChange("level2", e.target.value)}
        >
          {Object.values(data[selected["level1"]].enumerations).map(
            (value, index) => (
              <option value={value} key={index}>
                {value}
              </option>
            )
          )}
        </select>
      )}

      {/* Children - Level 2 */}
      {selected["level1"] && data[selected["level1"]]?.children && (
        <select
          className="select select-primary"
          onChange={(e) => handleChange("level2", e.target.value)}
        >
          {Object.keys(data[selected["level1"]].children).map(
            (value, index) => (
              <option value={value} key={index}>
                {value}
              </option>
            )
          )}
        </select>
      )}

      {/* Children - Level 3 */}
      {selected["level2"] &&
        data[selected["level1"]]?.children &&
        data[selected["level1"]]["children"][selected["level2"]]?.children && (
          <select
            className="select select-primary"
            onChange={(e) => handleChange("level3", e.target.value)}
          >
            {Object.keys(
              data[selected["level1"]]["children"][selected["level2"]].children
            ).map((value, index) => (
              <option value={value} key={index}>
                {value}
              </option>
            ))}
          </select>
        )}
    </div>
  );
};
