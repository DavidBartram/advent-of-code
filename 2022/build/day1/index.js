"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    Object.defineProperty(o, k2, { enumerable: true, get: function() { return m[k]; } });
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
Object.defineProperty(exports, "__esModule", { value: true });
const day_1 = require("../day");
const A = __importStar(require("fp-ts/Array"));
const function_1 = require("fp-ts/lib/function");
class Day1 extends day_1.Day {
    constructor() {
        super(1);
    }
    solveForPartOne(input) {
        return (0, function_1.pipe)(input, (x) => x.split("\n\n"), A.map((x) => x.split("\n")), A.map((0, function_1.flow)(A.map((x) => Number(x)), A.reduce(0, (acc, num) => acc + num))), (x) => Math.max(...x).toString());
    }
    solveForPartTwo(input) {
        return (0, function_1.pipe)(input, (x) => x.split("\n\n"), A.map((x) => x.split("\n")), A.map((0, function_1.flow)(A.map((x) => Number(x)), A.reduce(0, (acc, num) => acc + num))), (x) => x.sort((a, b) => b - a), (x) => (x[0] + x[1] + x[2]).toString());
    }
}
exports.default = new Day1();
