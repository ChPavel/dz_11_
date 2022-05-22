from flask import Flask, request, render_template
from candidates import Candidates

date = 'candidates.json'
app = Flask(__name__)
candidates = Candidates(date)


@app.route("/")                                                 # представление для роута "/"
def page_list_candidates():
    candidate = candidates.load_date()
    return render_template('list.html', candidate=candidate)


@app.route("/candidate/<int:candidate_id>/")                    # представление для роута "/candidate/<int:candidate_id>/"
def page_candidate(candidate_id):
    choiсe = candidates.choiсe_id(id=candidate_id)
    if choiсe == None:
        return f"База содержит всего {len(candidates.load_date())} кандидатов"
    return render_template('card.html', candidate=choiсe)


@app.route("/search/<candidate_name>/")                          # представление для роута "/search/<candidate_name>/"
def page_search_result_names(candidate_name):
    search_result = candidates.search_result(name_search=candidate_name)
    number_of_found = len(search_result)
    if len(search_result) == 0:
        return f"Среди кандидатов нет специалистов с именем '{candidate_name}'."
    return render_template('search.html', candidate=search_result, number=number_of_found)


@app.route("/skill/<skill_name>/")                              # представление для роута "/skill/<skill_name>/"
def page_search_result_skills(skill_name):
    search_result = candidates.choiсe_skills (skill=skill_name)
    number_of_found = len(search_result)
    if len(search_result) == 0:
        return f"Среди кандидатов нет специалистов с навыком '{skill_name}'."
    return render_template('skill.html', candidate=search_result, skill_name=skill_name, number=number_of_found)


if __name__ == '__main__':
    app.run(host='127.0.0.2', port=8000)

