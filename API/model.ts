import { Sequelize, DataTypes, Model, InferAttributes, InferCreationAttributes, CreationOptional } from "sequelize";
import sequelize from "connectdb";

export default class Routes extends Model<InferAttributes<Routes>, InferCreationAttributes<Routes>> {
    declare id: CreationOptional<number>;
    declare date: Date;
    declare user: string;
    declare photo: string;
    declare name: string;
    declare desc: string;
    declare grade: string;
    declare angle: string;
    declare layout: CreationOptional<string>;
}

Routes.init({
    id: {
        type: DataTypes.INTEGER,
        primaryKey: true,
        autoIncrement: true,
    },
    date: {
        type: DataTypes.DATE,
        allowNull: false,
    },
    user: {
        type: DataTypes.STRING,
        allowNull: false,
    },
    photo: {
        type: DataTypes.STRING,
        allowNull: false,
    },
    name: {
        type: DataTypes.STRING,
        allowNull: false,
    },
    desc: {
        type: DataTypes.STRING,
    },
    grade: {
        type: DataTypes.STRING,
        allowNull: false,
    },
    angle: {
        type: DataTypes.STRING,
        allowNull: false,
    },
    layout: {
        type: DataTypes.STRING,
        allowNull: false,
        defaultValue: "2024/2025",
    },
    },
    {
        sequelize,
        timestamps: false,
        tableName: 'routes',
    }
)
