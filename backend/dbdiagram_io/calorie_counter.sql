CREATE TABLE "CustomUser" (
  "id" integer PRIMARY KEY,
  "username" varchar UNIQUE,
  "email" varchar UNIQUE,
  "password" varchar,
  "is_staff" boolean,
  "is_active" boolean,
  "date_joined" timestamp
);

CREATE TABLE "TextHistory" (
  "id" integer PRIMARY KEY,
  "fdc_id" integer NOT NULL,
  "seq_num" integer,
  "user_id" integer,
  "text" varchar
);

CREATE TABLE "Foods" (
  "fdc_id" integer PRIMARY KEY,
  "description" varchar,
  "food_category_id" integer NOT NULL
);

CREATE TABLE "FoodCateogry" (
  "food_category_id" integer PRIMARY KEY,
  "description" varchar
);

CREATE TABLE "FoodPortions" (
  "id" integer PRIMARY KEY,
  "fdc_id" integer NOT NULL,
  "seq_num" varchar,
  "description" varchar,
  "gram_weight" float
);

CREATE TABLE "FoodNutrients" (
  "fdc_id" integer PRIMARY KEY,
  "nutrient_id" integer NOT NULL,
  "amount" float
);

CREATE TABLE "Nutrients" (
  "nutrient_id" integer PRIMARY KEY,
  "name" varchar,
  "unit_name" varchar,
  "rank" float
);

CREATE TABLE "Ingredients" (
  "id" integer PRIMARY KEY,
  "fdc_id" integer,
  "seq_num" integer,
  "description" varchar,
  "gram_weight" float
);

ALTER TABLE "TextHistory" ADD FOREIGN KEY ("user_id") REFERENCES "CustomUser" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "TextHistory" ADD FOREIGN KEY ("fdc_id") REFERENCES "Foods" ("fdc_id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "Foods" ADD FOREIGN KEY ("food_category_id") REFERENCES "FoodCateogry" ("food_category_id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "FoodPortions" ADD FOREIGN KEY ("fdc_id") REFERENCES "Foods" ("fdc_id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "FoodNutrients" ADD FOREIGN KEY ("fdc_id") REFERENCES "Foods" ("fdc_id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "FoodNutrients" ADD FOREIGN KEY ("nutrient_id") REFERENCES "Nutrients" ("nutrient_id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "Ingredients" ADD FOREIGN KEY ("fdc_id") REFERENCES "Foods" ("fdc_id") DEFERRABLE INITIALLY IMMEDIATE;
