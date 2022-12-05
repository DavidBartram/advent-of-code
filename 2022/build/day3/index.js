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
const immutable_1 = require("immutable");
class Day3 extends day_1.Day {
    constructor() {
        super(3);
    }
    spliceArrayIntoChunks(arr, chunkSize) {
        const res = [];
        while (arr.length > 0) {
            const chunk = arr.splice(0, chunkSize);
            res.push(chunk);
        }
        return res;
    }
    solveForPartOne(input) {
        return (0, function_1.pipe)(input, (x) => x.split("\n"), A.map((x) => {
            const mid = x.length / 2;
            return { left: (0, immutable_1.Set)(x.slice(0, mid)), right: (0, immutable_1.Set)(x.slice(mid)) };
        }), A.map((x) => x.left.intersect(x.right).first("")), A.reduce(0, (acc, char) => {
            if (char === char.toUpperCase()) {
                return acc + char.charCodeAt(0) - 38;
            }
            else {
                return acc + char.charCodeAt(0) - 96;
            }
        }), (x) => x.toString());
    }
    solveForPartTwo(input) {
        return (0, function_1.pipe)(input, (x) => this.spliceArrayIntoChunks(x.split("\n"), 3), A.map((x) => ({ left: (0, immutable_1.Set)(x[0]), middle: (0, immutable_1.Set)(x[1]), right: (0, immutable_1.Set)(x[2]) })), A.map((x) => x.left.intersect(x.middle).intersect(x.right).first("")), A.reduce(0, (acc, char) => {
            if (char === char.toUpperCase()) {
                return acc + char.charCodeAt(0) - 38;
            }
            else {
                return acc + char.charCodeAt(0) - 96;
            }
        }), (x) => x.toString());
    }
}
exports.default = new Day3();
