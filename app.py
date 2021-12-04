from flask import Flask, render_template, request
import math

app = Flask(__name__, template_folder="./templates", static_url_path="/static")


@app.route("/", methods=["POST", "GET"])
def Calculate():
    bmr = ""
    bodyFat = ""
    tdde = ""
    tdde_for_musclebuilding = ""
    Calories_for_musclebuilding = ""
    bodyType = ""
    cabohydrate = ""
    protein = ""
    fats = ""
    comment = ""
    if (
        request.method == "POST"
        and "weight" in request.form
        and "height" in request.form
        and "age" in request.form
        and "gender" in request.form
        and "waist" in request.form
        and "neck" in request.form
        and "hip" in request.form
        and "activity_level" in request.form
        and "weight-goal" in request.form
    ):
        weight = float(request.form.get("weight"))
        height = float(request.form.get("height"))
        age = float(request.form.get("age"))
        gender = str(request.form["gender"])
        hip = float(request.form.get("hip"))
        neck = float(request.form.get("neck"))
        waist = float(request.form.get("waist"))
        activity_level = request.form["activity_level"]
        # weight_goal = float(request.form.get("weight-goal"))

        if gender == "male":

            bmr = (10 * float(weight)) + (6.25 * float(height)) - (5 * float(age)) + 5

            tdde = bmr * float(activity_level)

            bodyFat = (
                495
                / (
                    1.0324
                    - 0.19077 * math.log10(float(waist) - float(neck))
                    + 0.15456 * math.log10(float(height))
                )
                - 450
            )
            if age <= 21 and bodyFat == 22:
                comment = "good"
            elif age <= 29 and bodyFat == 23:
                comment = "good"
            elif age <= 39 and bodyFat == 24:
                comment = "good"
            elif age > 39 and bodyFat == 26:
                comment = "Fine!"
            else:
                comment = " Do exercise! "

            #     Age 18 to 21 - 22% for males, 33% for females;
            #     Age 22 to 29 - 23% for males, 34% for females;
            #     Age 30 to 39 - 24% for males, 35% for females;
            #     Age over 40 - 26% for males, 36% for females

            ############# ====> BUILD MUSCLE <======= ###############
            bmr_for_muscle = (
                66
                + (6.2 * float(weight))
                + (12.7 * float(height))
                - (6.76 * float(age))
            )

            tdde_for_musclebuilding = bmr_for_muscle * float(activity_level)

            # ```You’re here to pack on size, so you’ll need to
            #    increase the number of calories
            #    you eat each day by 15% more than your TDEE```

            Calories_for_musclebuilding = tdde_for_musclebuilding * 0.15

            total_calo_to_build = tdde_for_musclebuilding + Calories_for_musclebuilding

            if bodyType == "ENDOMORPH BODY":

                cabohydrate = (total_calo_to_build * 0.25) / 4

                protein = (total_calo_to_build * 0.40) / 4

                fats = (total_calo_to_build * 0.35) / 9

            if bodyType == "ECTOMORPH BODY":

                cabohydrate = (total_calo_to_build * 0.40) / 4

                protein = (total_calo_to_build * 0.30) / 4

                fats = (total_calo_to_build * 0.30) / 9

            if bodyType == "MESOMORPH BODY TYPE":

                cabohydrate = (total_calo_to_build * 0.40) / 4

                protein = (total_calo_to_build * 0.35) / 4

                fats = (total_calo_to_build * 0.25) / 9

        #########3======> ENDING (BUILD MUSCLE FOR MALE) <===========###########

        if gender == "female":

            bmr = (10 * float(weight)) + (6.25 * float(height)) - (5 * float(age)) - 161

            tdde = bmr * float(activity_level)

            bodyFat = (
                495
                / (
                    1.29579
                    - 0.35004 * math.log10(float(waist) + float(hip) - float(neck))
                    + 0.22100 * math.log10(float(height))
                )
                - 450
            )

            ############# ADVICE FOR USER ###############
            if age <= 21 and bodyFat == 33:
                comment = "good"
            elif age <= 29 and bodyFat == 34:
                comment = "good"
            elif age <= 39 and bodyFat == 35:
                comment = "good"
            elif age > 39 and bodyFat == 36:
                comment = "Fine!"
            else:
                comment = " Do exercise! "
            ##################### - *** -#################

            ############# ====> BUILD MUSCLE <======= ###############
            bmr_for_muscle = (
                655.1
                + (4.35 * float(weight))
                + (4.7 * float(height))
                - (4.7 * float(age))
            )

            tdde_for_musclebuilding = bmr_for_muscle * float(activity_level)

            # ```You’re here to pack on size, so you’ll need to
            #    increase the number of calories
            #    you eat each day by 15% more than your TDEE```

            Calories_for_musclebuilding = tdde_for_musclebuilding * 0.15

            total_calo_to_build = tdde_for_musclebuilding + Calories_for_musclebuilding

            if bodyType == "ENDOMORPH BODY":

                cabohydrate = (total_calo_to_build * 0.25) / 4

                protein = (total_calo_to_build * 0.40) / 4

                fats = (total_calo_to_build * 0.35) / 9

            if bodyType == "ECTOMORPH BODY":

                cabohydrate = (total_calo_to_build * 0.40) / 4

                protein = (total_calo_to_build * 0.30) / 4

                fats = (total_calo_to_build * 0.30) / 9

            if bodyType == "MESOMORPH BODY TYPE":

                cabohydrate = (total_calo_to_build * 0.40) / 4

                protein = (total_calo_to_build * 0.35) / 4

                fats = (total_calo_to_build * 0.25) / 9
    #########3======> ENDING (BUILD MUSCLE FOR FEMALE) <===========###########

    return render_template(
        "index.html",
        bmr=bmr,
        bodyFat=bodyFat,
        tdde=tdde,
        tdde_for_musclebuilding=tdde_for_musclebuilding,
        Calories_for_musclebuilding=Calories_for_musclebuilding,
        cabohydrate=cabohydrate,
        protein=protein,
        fats=fats,
        comment=comment,
    )


if __name__ == "__main__":
    app.run(debug=True)
