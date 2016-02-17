EMPLOYEES = (('',''),
          ('Robert', 'Robert'),
          ('Denis', 'Denis'),
          ('Steve', 'Steve'),
          ('Andrew','Andrew'),
          ('Floriante','Floriante'),
          ('Kennedy','Kennedy'),
          ('Sylvia','Sylvia'),
          ('Josh', 'Josh'),
          ('Micheal', 'Micheal'),
          ('Kitamirike','Kitamirike'),
          ('Joy','Joy'),
          ('Patrick', 'Patrick'),
)

SET =    (('True', 'Yes'),
          ('False', 'No')
)


'''
add search feature
validation : same title error,
	     date signed
	     return errors
	     valid contact
	     success message, 


{% if ctc_form.errors %}
    {% for field in ctc_form %}
	{% for error in field.errors %}   
            <div class="alert alert-error">
		<strong class="alert-font"> {{ error|escape }} </strong>
	    </div>
	{% endfor %}
    {% endfor %}
{% endif %}
'''

