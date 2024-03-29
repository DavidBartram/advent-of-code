"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const index_1 = __importDefault(require("./day0/index"));
const index_2 = __importDefault(require("./day1/index"));
const index_3 = __importDefault(require("./day2/index"));
const index_4 = __importDefault(require("./day3/index"));
// MORE IMPORTS HERE
const days = [
    index_1.default,
    index_2.default,
    index_3.default,
    index_4.default,
    // MORE DAYS HERE
];
async function runDay(dayId) {
    const resultPart1 = await days[dayId].partOne();
    console.log("Part 1 result:\n");
    console.log(resultPart1);
    console.log("\n");
    const resultPart2 = await days[dayId].partTwo();
    console.log("Part 2 result:\n");
    console.log(resultPart2);
}
console.log("\n\n\n   ADVENT OF CODE 2022 \n\n");
const params = process.argv.splice(2);
if (params.length) {
    runDay(parseInt(params[0], 10));
}
else {
    console.log(`Usage: npm run start [day]`);
    console.log(`Available days: [ ${days.map((x) => x.id).join(", ")} ]`);
}
