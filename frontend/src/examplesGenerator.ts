import { JsonSchema } from "@jsonforms/core";

const exampleGetters = {
  string: (item: any) => item.example || "string",
  number: (item: any) => item.example || 1,
  integer: (item: any) => item.example || 1,
  boolean: (item: any) => item.example || false,
  null: (item: any) => item.example || null,
} as Record<string, any>;

export const exampleGenerator = (
  schema: JsonSchema
): Record<string, any> | string => {
  const resultData = {} as Record<string, any>;
  if (!schema.properties) return "string";
  for (const property in schema.properties) {
    const propertyValue = schema.properties[property];
    if (propertyValue.type == "object") {
      resultData[property] = exampleGenerator(propertyValue);
    } else if (propertyValue.type == "array") {
      resultData[property] = [
        exampleGenerator(propertyValue.items as JsonSchema),
      ];
    } else {
      resultData[property] =
        exampleGetters[propertyValue.type as string](propertyValue);
    }
  }
  return resultData;
};
